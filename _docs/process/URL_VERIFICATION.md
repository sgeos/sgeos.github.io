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
| Securities and Exchange Commission | sec.gov | Includes EDGAR search and the Archives document paths |
| Congressional Research Service | crsreports.congress.gov, congress.gov | Federal bot-detection |
| Government Accountability Office | gao.gov | Federal bot-detection |
| Space Force | spaceforce.mil | Federal bot-detection, consistent with other .mil hosts |
| Department of Defense | defense.gov | Federal bot-detection |
| Bloomberg | bloomberg.com | Financial-press bot-detection |
| Breaking Defense | breakingdefense.com | Trade-press bot-detection |
| Nasdaq Listing Center | listingcenter.nasdaq.com | Exchange rulebook bot-detection |
| S and P Global | spglobal.com | Index-provider bot-detection |
| Tesla Investor Relations | ir.tesla.com | Corporate investor-relations bot-detection |
| National Venture Capital Association | nvca.org | Trade-association bot-detection |
| OpenAI | openai.com | Corporate bot-detection, observed 2026-08-02 |
| Academic publishers | jstor.org, sciencedirect.com, onlinelibrary.wiley.com, academic.oup.com, journals.uchicago.edu, mitpress.mit.edu, jhupbooks.press.jhu.edu, liebertpub.com, pubsonline.informs.org, cambridge.org, sup.org, e-elgar.com, simonandschuster.com, si.edu | Publisher bot-detection across the set |

If a new 403 site appears during a publication, add it to this catalogue with one line of context.

## Other Non-200 Responses That Are Not Failures

| Code | Site | Meaning |
|------|------|---------|
| 202 | eur-lex.europa.eu | Accepted while the document renders. The document is present. |
| 401 | wsj.com | Paywall. The URL is canonical. |
| 429 | blueorigin.com | Persistent rate-limit response to curl rather than a transient one. Retried after a pause and still 429, so treat as bot-detection rather than as a dead link. |
| connection reset | washingtonpost.com | Blocks curl outright. Verify by web search. |

Two hosts rate-limit aggressive sweeps and will make every link look dead if paced too tightly. `openlibrary.org` is the worst offender and `blueorigin.com` the second. Pace verification or isolate the suspect URL and retest it alone before concluding anything is broken.

## An HTTP 200 Does Not Verify a Citation

A status check confirms that a URL resolves. It does not confirm that the document at the other end is the work the citation names. Those are different properties, and the second is the one that matters.

An audit on 2026-08-02 across the History of SpaceX corpus found **thirteen citations whose anchor title and target document did not correspond at all**. Each URL returned HTTP 200. Several pointed at real, well-formed journal articles by unrelated authors on unrelated subjects. A link-status sweep of any depth would have passed every one of them.

Check DOI-bearing citations against the registry rather than against the HTTP status.

```sh
# does the DOI resolve at all? no redirect means it was constructed
curl -sI "https://doi.org/10.xxxx/yyyy" | grep -i '^location:'

# does the registered work match the citation?
curl -s "https://api.crossref.org/works/10.xxxx/yyyy" \
  | python3 -c "import json,sys; m=json.load(sys.stdin)['message']; \
    print(m.get('title'), [a.get('family') for a in m.get('author',[])], m.get('issued'))"
```

Two distinct failure modes appeared, and both are invisible to a status check.

- **Unregistered DOI.** `doi.org` returns no redirect. The identifier was fabricated. The containing URL may still return 200 because the publisher serves a generic page for unknown paths.
- **Mismatched DOI.** The identifier resolves to a real paper that is not the cited one. This is the more dangerous case, because every automated check passes and only reading the target reveals it.

Never introduce a citation whose target you have not confirmed names the work you are citing. When a source cannot be confirmed, drop it. A missing citation is a gap; a confident citation pointing at the wrong document is a fabrication, and it is worse than the gap it was added to fill.

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
