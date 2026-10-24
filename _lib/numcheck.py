#!/usr/bin/env python3
"""Harness for independently re-deriving every value an article states.

NAMED `numcheck` AND NOT `numbers`. The obvious name shadows the standard
library's `numbers` module, and because article scripts put `_lib` first on
`sys.path`, that shadowing broke `statistics` for every caller through the
`fractions` import chain. A stdlib-collision test now guards the whole package.

Eighteen `verify_numbers.py` copies share this harness and differ only in the
physics. THE HARNESS IS EXTRACTED AND THE PHYSICS IS NOT, because the equations
are the article's argument and abstracting them would remove the point.

THE DISCIPLINE THE HARNESS ENFORCES, stated once instead of in eighteen
docstrings.

  DO NOT IMPORT THE ARTICLE'S OWN CALCULATION. Constants are re-entered by hand
  and relations re-typed from the article's displayed equations. An import makes
  a shared algebraic slip cancel instead of showing up as a disagreement.

  PREFER A DIFFERENT ROUTE. Where a value can be reached by bisection, by
  scanning, by simulation or by a closed form, use the one the article did not.
  A323 caught a stall speed that was wrong by five miles per hour this way.

  PREFER A PROPERTY OVER A POINT. `prop` tests a claimed relation over many
  randomised inputs. A369's dispersion bound was checked over 20,000 random
  corpora rather than at the one point the article quoted.

  REQUIRE EVERY VALUE TO APPEAR IN THE DRAFT. `require_in_text` fails when a
  verified number is absent from the prose, which catches the case where a
  verifier drifts away from the article it is supposed to be checking.
"""

import math
import random
import re


class Checker:
    def __init__(self, label="verification", seed=20260101):
        self.label = label
        self.ok = 0
        self.failures = []
        self.values = []
        self.rng = random.Random(seed)

    def chk(self, name, stated, computed, tol=0.02, unit=""):
        """Relative-tolerance comparison. Records the stated value for later."""
        if stated == 0:
            rel = abs(computed)
        else:
            rel = abs(computed - stated) / abs(stated)
        self.values.append((name, stated))
        if rel <= tol:
            self.ok += 1
        else:
            self.failures.append(f"{name}: stated {stated:.6g}, computed {computed:.6g} "
                                 f"({rel*100:.2f}% off, tol {tol*100:.2f}%) {unit}")
        return rel <= tol

    def exact(self, name, stated, computed):
        self.values.append((name, stated))
        if stated == computed:
            self.ok += 1
            return True
        self.failures.append(f"{name}: stated {stated!r}, computed {computed!r}")
        return False

    def prop(self, name, predicate, gen, trials=10000):
        """Assert a property over randomised inputs rather than at one point."""
        bad = 0
        example = None
        for _ in range(trials):
            x = gen(self.rng)
            try:
                held = predicate(x)
            except Exception as e:
                held, x = False, f"{x!r} raised {e}"
            if not held:
                bad += 1
                if example is None:
                    example = x
        if bad:
            self.failures.append(f"{name}: property failed {bad}/{trials}, e.g. {example!r}")
            return False
        self.ok += 1
        return True

    def bisect(self, name, stated, f, lo, hi, tol=0.02, iters=200):
        """Recover a root by bisection, a different route from a closed form."""
        flo = f(lo)
        for _ in range(iters):
            mid = (lo + hi) / 2.0
            fm = f(mid)
            if (fm < 0) == (flo < 0):
                lo, flo = mid, fm
            else:
                hi = mid
        return self.chk(name, stated, (lo + hi) / 2.0, tol)

    def require_in_text(self, path, fmt=lambda v: f"{v:g}"):
        """Every verified value must appear in the draft, else the two drifted."""
        text = open(path, encoding="utf-8").read()
        flat = re.sub(r"[,\s]", "", text)
        missing = []
        for name, v in self.values:
            if isinstance(v, str):
                if v not in text:
                    missing.append(f"{name} ({v!r})")
                continue
            if re.sub(r"[,\s]", "", fmt(v)) not in flat:
                missing.append(f"{name} ({fmt(v)})")
        if missing:
            self.failures.append(f"{len(missing)} verified values absent from the draft: "
                                 + ", ".join(missing[:6]))
        return not missing

    def report(self):
        total = self.ok + len(self.failures)
        for f in self.failures:
            print(f"  FAIL  {f}")
        print(f"{self.ok}/{total} checks passed  [{self.label}]")
        return not self.failures


def rel_error(a, b):
    return abs(a - b) / abs(b) if b else abs(a)


def close(a, b, tol=0.02):
    return rel_error(a, b) <= tol


# ------------------------------------------------------------------ claims
#
# WHY. A378 to A384 each carried a `numbers.py` that only printed, and the
# values reached the prose by hand. Nothing tied a computed value to the text,
# which is the defect class `_lib/survey.py` was written for: a presence check
# goes green precisely when a number goes stale. A claims file states, for each
# number the article prints, how to compute it and where the article says it,
# and `check` recomputes every value on every run. Recomputing in-process also
# removes the stale-intermediate class, a `numbers.json` agreeing with a stale
# article, because there is no intermediate.
#
# A CLAIMS FILE is a Python module, because the computation is code.
#
#   DRAFT = "_drafts/x.markdown"          # optional, the command line may give it
#   CLAIMS = [
#       Claim("flux-ratio", lambda: ((1 + E) / (1 - E)) ** 2,
#             pattern=r"which is ([\d.]+) times its value at aphelion"),
#   ]
#   FORBIDDEN = ["withdrawn wording"]     # optional, must not appear
#   REQUIRED = ["replacement wording"]    # optional, must appear
#
# THE RULES IT ENFORCES, each from a recorded defect.
#
#   TOLERANCE COMES FROM THE PRINTED DIGITS. "6.5" stands for anything that
#   rounds to it, so the tolerance is half a unit in the last printed place,
#   widened by 1e-6 for float noise at the rounding boundary. A fixed relative
#   tolerance raised eleven false failures in A363 and passed real errors in
#   coarse values.
#
#   A PATTERN THAT MATCHES NOTHING FAILS. A334 reported 47 of 47 passing while
#   twelve values were absent, and an A352 scanner parsed zero candidates.
#
#   EVERY OCCURRENCE CARRIES THE VALUE, by default. A second, stale copy of a
#   number satisfies a presence check.
#
#   EVERY CLAIM MUST BE ABLE TO FAIL. `inject` alters each stated value in the
#   text and requires its claim to fail, so a claim whose pattern or tolerance
#   makes it vacuous is reported.
#
#   SPELLED NUMBERS, SEPARATORS AND MINUS SIGNS ARE NUMBERS. "twenty-one",
#   "2,207", "2{,}207" and "−3" are all read.
#
#   THE CLAIMS FILE MUST NOT IMPORT THE ARTICLE'S CALCULATION. A335 had the
#   same two wrong constants in its calculation and its verifier.

import importlib.util
import os
import sys


class Claim:
    """One number the article states. See the module notes for the rules."""

    def __init__(self, cid, compute, pattern, occurrences="all", tol="printed", scale=1.0,
                 alt=None, scope="prose", note=""):
        if not callable(compute):
            raise TypeError(f"{cid}: compute must be callable")
        if re.compile(pattern).groups != 1:
            raise ValueError(f"{cid}: pattern needs exactly one capture group, the stated value")
        if not (occurrences == "all" or (isinstance(occurrences, int) and occurrences >= 1)):
            raise ValueError(f"{cid}: occurrences is 'all' or a positive count")
        if scope not in ("prose", "all"):
            raise ValueError(f"{cid}: scope is 'prose' or 'all'")
        self.id, self.compute, self.pattern, self.occurrences = cid, compute, pattern, occurrences
        self.tol, self.scale, self.alt, self.scope, self.note = tol, scale, alt, scope, note


_SPELLED = re.compile(r"^[a-z\s-]+$")


def parse_stated(s):
    """The number a printed string states, or None. Handles the forms the corpus uses."""
    # A capture such as `[\d.]+` takes a closing full stop with it.
    t = (s or "").strip().rstrip(".,;:").replace("−", "-").replace("{,}", "").replace(" ", "")
    t = t.replace(" ", "").replace(" ", "")
    if _SPELLED.match(t.lower()):
        import survey
        return survey.words_to_int(t)
    t = t.replace(",", "").rstrip("%")
    try:
        return int(t) if re.fullmatch(r"-?\d+", t) else float(t)
    except ValueError:
        return None


def printed_tolerance(s):
    """Half a unit in the last printed place, plus 1e-6 relative slack for float noise."""
    t = (s or "").strip().rstrip(".,;:").replace("{,}", "").replace(",", "").rstrip("%")
    if _SPELLED.match(t.lower()):
        return 0.5
    m = re.search(r"\.(\d+)", t)
    return 0.5 * 10 ** (-len(m.group(1))) if m else 0.5


def _agrees(claim, stated_text, stated, computed):
    if claim.tol == "exact":
        return stated == computed
    if claim.tol == "printed":
        return abs(stated - computed) <= printed_tolerance(stated_text) + 1e-6 * abs(computed)
    kind, x = claim.tol
    if kind == "rel":
        return abs(stated - computed) <= x * abs(computed)
    if kind == "abs":
        return abs(stated - computed) <= x
    raise ValueError(f"{claim.id}: tol is 'printed', 'exact', ('rel', x) or ('abs', x)")


def searchable(text, scope="prose"):
    """The article body with references and code removed and line breaks flattened.

    HARD-WRAPPED TEXT GAVE A COUNT OF ZERO in A364, because a pattern written
    on one line never matched a phrase broken across two. `prose` also removes
    display and inline mathematics.
    """
    import post
    body = post.strip_code(post.body(text))
    if scope == "prose":
        body = post.strip_math(body)
    return re.sub(r"\s+", " ", body)


def check_claims(text, claims, forbidden=(), required=()):
    """[(claim id, ok, detail)] for every claim and phrase rule."""
    out = []
    flat = {s: searchable(text, s) for s in ("prose", "all")}
    for c in claims:
        try:
            computed = c.compute()
            if c.alt is not None:
                other = c.alt()
                if abs(other - computed) > 1e-9 * max(1.0, abs(computed)):
                    out.append((c.id, False, f"routes disagree, {computed!r} against {other!r}"))
                    continue
        except Exception as e:  # noqa: BLE001  a crashing computation is a failed claim
            out.append((c.id, False, f"compute raised {type(e).__name__}: {e}"))
            continue
        hits = list(re.finditer(c.pattern, flat[c.scope]))
        if not hits:
            out.append((c.id, False, "pattern matched nothing, so nothing was checked"))
            continue
        if c.occurrences != "all" and len(hits) != c.occurrences:
            out.append((c.id, False, f"{len(hits)} occurrences, expected {c.occurrences}"))
            continue
        bad = []
        for m in hits:
            stated = parse_stated(m.group(1))
            if stated is None:
                bad.append(f"unreadable {m.group(1)!r}")
            elif not _agrees(c, m.group(1), stated * c.scale, computed):
                bad.append(f"states {m.group(1)}, computed {computed:.6g}")
        out.append((c.id, not bad, "; ".join(bad) if bad else
                    f"{len(hits)} occurrence(s) agree with {computed:.6g}"))
    for phrase in forbidden:
        n = len(re.findall(re.escape(phrase), flat["all"]))
        out.append((f"forbidden: {phrase[:40]}", n == 0, f"{n} occurrence(s)"))
    for phrase in required:
        n = len(re.findall(re.escape(phrase), flat["all"]))
        out.append((f"required: {phrase[:40]}", n > 0, f"{n} occurrence(s)"))
    return out


def _mutate(s):
    """The printed value with its last digit moved by more than its tolerance."""
    m = re.search(r"(\d)(?!.*\d)", s)
    if not m:
        return None
    d = int(m.group(1))
    return s[:m.start()] + str((d + 5) % 10) + s[m.end():]


def inject(text, claims):
    """Claims that still pass when their stated value is altered, which makes them vacuous.

    Each claim's first match is altered in the flattened text, by five in its
    last digit, and the claim is re-run on that text alone. Spelled numbers are
    skipped, since a word has no last digit.
    """
    vacuous = []
    for c in claims:
        flat = searchable(text, c.scope)
        m = re.search(c.pattern, flat)
        if not m or _mutate(m.group(1)) is None:
            continue
        bent = flat[:m.start(1)] + _mutate(m.group(1)) + flat[m.end(1):]
        probe = Claim(c.id, c.compute, c.pattern, c.occurrences, c.tol, c.scale, None, "all")
        if all(ok for _id, ok, _d in check_claims(bent, [probe])):
            vacuous.append(c.id)
    return vacuous


def load_claims(path):
    """The claims module at `path`. Refuses one that imports an article calculation."""
    src = open(path, encoding="utf-8").read()
    if re.search(r"^\s*(?:from|import)\s+(?:calc\w*|numbers_\w*)\b", src, re.M):
        raise ValueError(f"{path} imports an article calculation; re-enter the constants instead")
    spec = importlib.util.spec_from_file_location("claims_" + os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not isinstance(getattr(mod, "CLAIMS", None), list) or not mod.CLAIMS:
        raise ValueError(f"{path} defines no CLAIMS list")
    return mod


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(prog="numcheck.py", description="Recompute every number a claims file names.")
    ap.add_argument("command", choices=["check"])
    ap.add_argument("claims")
    ap.add_argument("draft", nargs="?")
    ap.add_argument("--inject", action="store_true", help="also prove each claim can fail")
    a = ap.parse_args(argv[1:])
    try:
        mod = load_claims(a.claims)
        draft = a.draft or getattr(mod, "DRAFT", None)
        if not draft:
            raise ValueError("no draft given in the claims file or on the command line")
        text = open(draft, encoding="utf-8").read()
    except (OSError, ValueError, SyntaxError) as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1
    rows = check_claims(text, mod.CLAIMS, getattr(mod, "FORBIDDEN", ()), getattr(mod, "REQUIRED", ()))
    for cid, ok, detail in rows:
        print(f"  {'ok  ' if ok else 'FAIL'}  {cid}: {detail}")
    failed = sum(1 for _c, ok, _d in rows if not ok)
    if a.inject:
        vac = inject(text, mod.CLAIMS)
        for cid in vac:
            print(f"  FAIL  {cid}: still passes with its stated value altered, so it checks nothing")
        failed += len(vac)
    print(f"{len(rows) - sum(1 for _c, ok, _d in rows if not ok)}/{len(rows)} passed, {failed} failure(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv))
