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
