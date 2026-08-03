# Forward-Dated and Back-Dated Posts

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

How posts with dates other than the current day behave on the live site, given the
`future: false` setting in `_config.yml`.

## Configuration

The site sets `future: false` in `_config.yml`, at line 86. The relevant excerpt:

```yaml
# Exclude posts dated in the future relative to build time. Forward-dated posts
# become eligible as their dates arrive, so a series unfolds on its own cadence
# without further pushes. The constraint this imposes is that a forward-dated
# post must not be the target of a post_url from a post whose date has passed,
# because the target is absent from the build until its own date arrives.
# Intra-cluster post_url references between forward-dated posts are safe
# because both sides are excluded together.
future: false
```

Forward-dated posts are **excluded from the build** until their date arrives. A deploy renders
only the posts whose dates have passed. As each date arrives, the next scheduled rebuild picks
that post up, so a dated series unfolds on its own without further pushes.

> **Correction, 2026-08-05.** This document previously stated that the site set `future: true`,
> quoted a configuration excerpt asserting it, and called that setting foundational. That was
> false, and it had been false for some time. Every claim below about visibility and about
> cross-references has been re-derived from the live configuration and verified against an
> actual Jekyll build. Commit `4cf5dd5` had set `future: true` at some earlier point; the live
> value is `false`.

## Forward-Dated Posts

A forward-dated post has a `date:` later than the build time.

- **Excluded from the deploy build.** It is not rendered.
- **Not visible at its direct URL.** The URL returns 404 until the date arrives.
- **Absent from the sitemap and from chronological listings** until the date arrives.
- Becomes visible at the first build that occurs on or after its date.

Observed on 2026-08-04: A292, dated 2026-08-04, returned 404 on a deploy that ran while eleven
sibling articles dated on or before the deploy date returned 200.

## Back-Dated Posts

A back-dated post has a `date:` earlier than the build time.

- Renders in the deploy build immediately.
- Visible at its direct URL and in chronological listings at its past date position.
- Unaffected by the `future:` setting, since its date has already passed.

The patents-and-startup series at A161 through A172 (dates 2026-05-03 through 2026-05-14,
published 2026-06-24) used the back-dated pattern.

## Cross-References Between Past and Future

**This is the build-failure interlock. Read it before writing any cross-reference.**

`{% post_url YYYY-MM-DD-slug %}` resolves against the posts **included in the build**. Under
`future: false` a forward-dated post is not included, so a `post_url` pointing at one does not
merely render a dead link. It **fails the entire site build**, not just the referring page.

Verified 2026-08-05 with a minimal two-post site under `future: false`:

```
Liquid Exception: Could not find post "2027-01-01-futurepost" in tag 'post_url'.
ERROR: YOUR SITE COULD NOT BE BUILT
```

The rules that follow from this:

- **Back-reference only.** A post may `post_url` a post whose date is earlier than its own.
  Forward references are written as plain prose with no link.
- **Intra-cluster references between forward-dated posts are safe**, because both sides are
  excluded together and both become eligible together.
- **A reference from an already-published post to a forward-dated post is the dangerous case.**
  The referring post is in the build, its target is not, and the build fails.
- Cross-linked drafts publish together or in strict date order. See
  [Cross-Linked Series](./CROSS_LINKED_SERIES.md).

## Visibility Considerations

Forward dating gives true invisibility until the date arrives, which is the behaviour the series
cadence relies on. A forward-dated series can be pushed once and will unfold day by day as each
date arrives, provided the site is rebuilt on that cadence.

**This depends on rebuilds happening after the push.** GitHub Pages rebuilds on push, not on a
timer. If no further commit lands, a forward-dated post may not appear on its date until some
later push triggers a build. Confirm a post is live on its date rather than assuming it.

If immediate visibility of future-dated work is ever required, that is a change to `_config.yml`,
which is a global setting affecting every forward-dated post on the site. It is a human-pilot
decision, not something to toggle for one deploy, and it would invalidate the back-reference-only
convention above.

## Series Application

- Forward-dated series at one article per day: use the incremental publication pattern from
  [Cross-Linked Series](./CROSS_LINKED_SERIES.md). Honour back-reference-only throughout.
- Back-dated series filling a calendar gap: use the batch publication pattern from
  [Cross-Linked Series](./CROSS_LINKED_SERIES.md). The articles deploy at their past positions
  immediately, and their mutual `post_url` references resolve because all are in the build.

Two independent series can run in parallel if their date ranges do not collide.

## Related Sections

- [Cross-Linked Series](./CROSS_LINKED_SERIES.md) for series-level publication patterns
- [Content Workflow](./CONTENT_WORKFLOW.md) for the per-article publication flow
- [Jekyll Structure](../architecture/JEKYLL_STRUCTURE.md) for site configuration
