"""Claims for A384, Mercury as a Colony and a Launch Site. A worked example and a test fixture.

Constants are re-entered here with their sources, not imported from any calculation.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from numcheck import Claim  # noqa: E402

DRAFT = "_posts/2026-08-20-mercury_as_colony_and_launch_site.markdown"

E_MERCURY = 0.2056            # orbital eccentricity, as the article states it
AU_M = 149_597_870_700        # astronomical unit, IAU 2012 Resolution B2, exact
JULIAN_YEAR_S = 365.25 * 86_400


def flux_ratio():
    """Perihelion over aphelion insolation, ((1 + e) / (1 - e)) squared."""
    return ((1 + E_MERCURY) / (1 - E_MERCURY)) ** 2


def flux_ratio_by_distances():
    """The same ratio from the two distances, a second route."""
    a = 1.0
    return (a * (1 + E_MERCURY)) ** 2 / (a * (1 - E_MERCURY)) ** 2


CLAIMS = [
    Claim("perihelion-flux-ratio", flux_ratio, alt=flux_ratio_by_distances,
          pattern=r"which is ([\d.]+) times its value at aphelion"),
    Claim("eccentricity-gives-ratio", flux_ratio,
          pattern=r"eccentricity of 0\.2056 gives the ratio of ([\d.]+)"),
    Claim("au-per-year", lambda: AU_M / JULIAN_YEAR_S / 1000,
          pattern=r"1 AU per year is ([\d.]+) kilometres per second", occurrences=1),
    Claim("eight-au-per-year", lambda: 8 * AU_M / JULIAN_YEAR_S / 1000,
          pattern=r"8 AU per year to about ([\d.]+) kilometres per second", tol=("abs", 0.5)),
]
