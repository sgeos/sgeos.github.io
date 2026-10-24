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

import os
import re
import sys


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


# ------------------------------------------------------------- edit files
#
# WHY A DATA FILE. A375 to A384 carried sixteen one-shot edit scripts and not one
# imported this module. Each re-declared a `rep` helper with an exact-match count
# assertion, which is the copy this module was extracted to end. A library is
# bypassed when using it costs more than retyping it, and a one-shot script
# costs nothing to retype. An edit file costs less than either, since it holds
# only the payload.
#
# WHY TOML LITERAL STRINGS. `'''...'''` takes no escapes, so `\mathcal` is one
# backslash on disk and one in the article. The doubled-backslash defect shipped
# in three consecutive articles through Python string literals that needed
# `\\mathcal`, and a format that cannot express the escape cannot get it wrong.
# A payload containing `'''` needs a basic string, and `load_edits` says so.
#
# THE FILE, with every key shown.
#
#   target = "_drafts/x.markdown"   # optional, the command line may give it
#   reflow = false                  # optional, reflow the post after applying
#
#   [[edit]]                        # replace exactly `count` matches, default 1
#   old = '''text to find'''
#   new = '''replacement'''
#   count = 1
#   note = "why"                    # optional, printed in the report
#
#   [[edit]]                        # insert after, or before, an anchor
#   after = '''anchor text'''       # or `before`
#   insert = '''inserted text'''
#
# Unknown keys are refused, because a misspelt `nwe` would otherwise be an edit
# that silently does nothing.

EDIT_KEYS = {"old", "new", "count", "note", "after", "before", "insert"}
FILE_KEYS = {"target", "reflow", "edit"}


def load_edits(path):
    """Edit specs from a TOML file. Raises EditError on any malformed entry."""
    import tomllib
    try:
        with open(path, "rb") as fh:
            doc = tomllib.load(fh)
    except tomllib.TOMLDecodeError as e:
        raise EditError(f"{path}: {e}. A payload containing ''' needs a basic string.") from e
    extra = set(doc) - FILE_KEYS
    if extra:
        raise EditError(f"{path}: unknown top-level keys {sorted(extra)}")
    specs = doc.get("edit")
    if not isinstance(specs, list) or not specs:
        raise EditError(f"{path}: no [[edit]] entries")
    for i, s in enumerate(specs):
        _check_spec(i, s)
    target = doc.get("target")
    if target is not None and not isinstance(target, str):
        raise EditError(f"{path}: target must be a string")
    if not isinstance(doc.get("reflow", False), bool):
        raise EditError(f"{path}: reflow must be true or false")
    return {"target": target, "reflow": doc.get("reflow", False), "edits": specs}


def _check_spec(i, s):
    if not isinstance(s, dict):
        raise EditError(f"edit {i}: not a table")
    extra = set(s) - EDIT_KEYS
    if extra:
        raise EditError(f"edit {i}: unknown keys {sorted(extra)}")
    for k in ("old", "new", "after", "before", "insert", "note"):
        if k in s and not isinstance(s[k], str):
            raise EditError(f"edit {i}: {k} must be a string")
    count = s.get("count", 1)
    if not isinstance(count, int) or isinstance(count, bool) or count < 1:
        raise EditError(f"edit {i}: count must be a positive integer")
    modes = [k for k in ("old", "after", "before") if k in s]
    if len(modes) != 1:
        raise EditError(f"edit {i}: exactly one of old, after, before is required")
    if modes[0] == "old" and ("new" not in s or "insert" in s):
        raise EditError(f"edit {i}: old needs new, and takes no insert")
    if modes[0] != "old" and ("insert" not in s or "new" in s or "count" in s):
        raise EditError(f"edit {i}: {modes[0]} needs insert, and takes no new or count")
    anchor = s[modes[0]]
    if not anchor.split():
        raise EditError(f"edit {i}: {modes[0]} is empty or whitespace")


def _plan(spec):
    """(find, make, done) for one spec.

    `find` is the pattern that must match `count` times, `make` builds the
    replacement from a match, and `done` is the pattern whose presence marks the
    edit as already applied, or None when only absence can show it.
    """
    if "old" in spec:
        new = spec["new"]
        find = match_ws(spec["old"])
        done = match_ws(new) if new.split() else None
        return find, (lambda _m, _n=new: _n), done
    if "after" in spec:
        anchor, ins = spec["after"], spec["insert"]
        return match_ws(anchor), (lambda m, _i=ins: m.group(0) + _i), match_ws(anchor + ins)
    anchor, ins = spec["before"], spec["insert"]
    return match_ws(anchor), (lambda m, _i=ins: _i + m.group(0)), match_ws(ins + anchor)


def _already_applied(text, spec, find, done):
    """True when every remaining match of `find` lies inside an applied result.

    A replacement whose new text contains its old text, which is how most
    insertions are written, still matches `old` after it is applied. Counting
    `old` alone would apply it twice on a rerun, so `old` must occur exactly as
    often as the applied text accounts for.
    """
    count = spec.get("count", 1)
    if done is None:
        return not find.search(text)
    n_done = len(done.findall(text))
    if n_done != count:
        return False
    inside = sum(len(find.findall(m.group(0))) for m in done.finditer(text))
    return len(find.findall(text)) == inside


def apply_specs(text, specs, rerun=False, guard_equations=True, guard_invariants=True):
    """Apply edit specs to text. Returns (new_text, report) or raises EditError.

    The contract is `apply_to_text`'s, all or nothing with every failure
    reported, plus two things the one-shot scripts did and it did not.

    RERUN. With `rerun`, an edit whose result is already present and whose
    target is absent is reported as already applied instead of failing. It is
    off by default, because with it on a target that moved for another reason
    reads as success whenever the replacement text happens to occur.

    THE INVARIANT GUARD COMPARES, it does not demand a clean file. A draft
    that already carries a lint defect could otherwise never be edited, even
    to fix that defect. A defect class that grows is refused.
    """
    import collections
    import lint
    eq_before = count_equations(text)
    before = collections.Counter(c for sev, c, _ in lint.scan(text) if sev == lint.DEFECT)
    out, failures, report = text, [], []
    for i, spec in enumerate(specs):
        _check_spec(i, spec)
        find, make, done = _plan(spec)
        count = spec.get("count", 1)
        label = " ".join((spec.get("note") or spec.get("old") or spec.get("after")
                          or spec.get("before")).split())[:60]
        # A SECOND RUN OF AN INSERTION STILL FINDS ITS ANCHOR and would insert
        # twice, so an applied edit is refused unless the rerun is declared.
        if _already_applied(out, spec, find, done):
            if rerun:
                report.append((i, "already applied", label))
            else:
                failures.append(f"edit {i}: already applied, pass --rerun to skip it: {label!r}")
            continue
        n = len(find.findall(out))
        if n != count:
            failures.append(f"edit {i}: matched {n} times, expected {count}: {label!r}")
            continue
        out = find.sub(make, out, count=count)
        report.append((i, "applied", label))
    if failures:
        raise EditError(f"{len(failures)} of {len(specs)} edits failed; nothing written\n  "
                        + "\n  ".join(failures))
    if guard_equations and count_equations(out) < eq_before:
        raise EditError(f"equation count dropped {eq_before} -> {count_equations(out)}; nothing written")
    if guard_invariants:
        after = collections.Counter(c for sev, c, _ in lint.scan(out) if sev == lint.DEFECT)
        grown = {c: (before[c], k) for c, k in after.items() if k > before[c]}
        if grown:
            raise EditError(f"edits introduce lint defects {grown}; nothing written")
    return out, report


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser(prog="edits.py", description="Apply a TOML edit file to a post.")
    ap.add_argument("command", choices=["apply", "check"],
                    help="apply writes the post; check reports what apply would do and writes nothing")
    ap.add_argument("edits", help="TOML edit file")
    ap.add_argument("target", nargs="?", help="post to edit, overriding the file's target")
    ap.add_argument("--rerun", action="store_true", help="treat edits whose result is present as done")
    ap.add_argument("--reflow", action="store_true", help="reflow after applying")
    ap.add_argument("--allow-equation-drop", action="store_true")
    ap.add_argument("--no-lint-guard", action="store_true")
    a = ap.parse_args(argv[1:])
    try:
        doc = load_edits(a.edits)
        target = a.target or doc["target"]
        if not target:
            raise EditError("no target given in the file or on the command line")
        text = open(target, encoding="utf-8").read()
        out, report = apply_specs(text, doc["edits"], rerun=a.rerun,
                                  guard_equations=not a.allow_equation_drop,
                                  guard_invariants=not a.no_lint_guard)
        if a.reflow or doc["reflow"]:
            import reflow as _reflow
            out = _reflow.reflow_post(out)
    except (EditError, OSError) as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1
    for i, status, label in report:
        print(f"  {i:3d}  {status:15s}  {label}")
    changed = out != text
    if a.command == "apply" and changed:
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(out)
    verb = "wrote" if a.command == "apply" and changed else "would write" if changed else "no change to"
    print(f"{verb} {target}: {sum(1 for r in report if r[1] == 'applied')} applied, "
          f"{sum(1 for r in report if r[1] != 'applied')} already applied")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(_main(sys.argv))
