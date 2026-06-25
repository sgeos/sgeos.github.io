# URL Verification

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The procedure for verifying every URL in an article responds correctly before publication.

## Procedure

Verify every URL with `curl -sI -o /dev/null -w "%{http_code}" -L --max-time 10` before publication. The script in [Style Verification](./STYLE_VERIFICATION.md) batches this across all URLs in a draft.

## Response Codes

- **200**: Acceptable. Includes 200 reached through a redirect chain.
- **302** or **307**: Acceptable when the redirect target itself returns 200. Some canonical fact-sheet URLs at NASA NSSDC redirect to the homepage under curl but serve correctly in browsers; treat these as known canonical even when the redirect chain is unfriendly.
- **403**: Acceptable only on known bot-detected canonical sources. See the catalogue below. The URL is the right one; the curl check is being blocked.
- **404**: Requires URL replacement before publication. Large organisations frequently reorganise their sites.
- **429**: Rate limiting. Wikipedia returns 429 under burst checks; the URL is valid. Retry individually if needed.
- **000**: Network failure or timeout. Retry; if persistent, find an alternative.

## URL Source Preference

Prefer canonical official URLs (.gov, .esa.int, .nasa.gov, .who.int, .iso.org, .ieee.org) over Wikipedia when the official URL works. The official source is more authoritative and less likely to be edited by external actors. Wikipedia is a reliable fallback when the official site has 404'd a page or moved it without a redirect.

IETF RFCs use the datatracker URL: `https://datatracker.ietf.org/doc/html/rfcXXXX`.

## Known 403 Canonical Sites

These canonical sources return 403 to curl due to bot-detection. The URL is the correct canonical URL and should be used despite the unfriendly response.

| Site | Domain | Notes |
|------|--------|-------|
| Edwards Air Force Base | edwards.af.mil | All .mil hosts commonly 403 to curl |
| Iridium Communications | iridium.com | Corporate Cloudflare protection |
| National Oceanic and Atmospheric Administration | noaa.gov | Federal bot-detection |
| NSF Standards Shop | nsf.org | Public catalogue page |
| International Atomic Energy Agency | iaea.org | Corporate bot-detection |
| American Society for Testing and Materials | astm.org | Standards body bot-detection |
| Transportation.gov | transportation.gov | Federal bot-detection |
| US Department of Energy | various sub-paths | Some sub-paths return 403 |
| Various .mil hosts | military.com et al. | Defense department bot-detection |

If a new 403 site appears during a publication, add it to this catalogue with one line of context.

## Common 404 Patterns

NASA, ESA, and similar organisations regularly relocate pages. Common patterns:

- NASA mission pages drift across `nasa.gov/missions/`, `nasa.gov/feature/`, `nasa.gov/centers/`, and `science.nasa.gov/missions/`. Try the Wikipedia article for the mission as a fallback.
- ESA pages drift across `esa.int/Science_Exploration/...` paths. Try the Wikipedia article for the mission.
- NSF program pages drift; try `usap.gov` or the Wikipedia article for an Antarctic Program reference.

When a 404 cannot be resolved to a canonical replacement, use the topical Wikipedia article and note in the article body that the canonical source has moved.

## Verification Script

See [Style Verification](./STYLE_VERIFICATION.md) for the batch URL-check script that processes every URL in a draft.

## Related Sections

- [Style Verification](./STYLE_VERIFICATION.md) for the verification scripts
- [Publication Review](./PUBLICATION_REVIEW.md) for the broader review pass
- [Style Guide](../writing/STYLE_GUIDE.md) for reference link conventions
