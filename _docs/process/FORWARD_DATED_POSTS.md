# Forward-Dated and Back-Dated Posts

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

How posts with dates other than the current day behave on the live site, given the `future: true` setting in `_config.yml`.

## Configuration

The site sets `future: true` in `_config.yml`. The relevant excerpt:

```yaml
# Publish posts dated in the future relative to the build time. Without this
# flag, Jekyll's default future: false silently excludes future-dated posts
# from the build, which breaks post_url cross-references to those posts and
# leaves committed work invisible until its date arrives. Setting future to
# true publishes all posts immediately regardless of date.
future: true
```

This setting is foundational. Without it, forward-dated posts would be excluded from the build, breaking `{% post_url %}` cross-references and leaving committed work invisible until the future date arrives. With it, all posts in `_posts/` are rendered at deploy time regardless of their `date:` field.

## Forward-Dated Posts

A forward-dated post has a `date:` later than the build time.

- Renders in the deploy build immediately.
- Visible at its direct URL and in the sitemap upon deploy.
- Appears at its future date position in chronological listings, so it sits "at the bottom" of the feed until its date arrives in real time.
- A reader browsing chronologically does not see the article until the date arrives. A reader visiting the URL directly sees it immediately.

The analog-facilities series at A152 through A160 (dates 2026-06-28 through 2026-07-06) used the forward-dated pattern.

## Back-Dated Posts

A back-dated post has a `date:` earlier than the build time.

- Renders in the deploy build immediately.
- Visible at its direct URL and in chronological listings at its past date position.
- Does not depend on `future: true`; it would deploy correctly even with `future: false`.

The patents-and-startup series at A161 through A172 (dates 2026-05-03 through 2026-05-14, published 2026-06-24) used the back-dated pattern.

## Cross-References Between Past and Future

`{% post_url YYYY-MM-DD-slug %}` resolves against any post in `_posts/` regardless of its date relative to the build time, as long as the file exists. A back-dated post may reference a forward-dated post by Liquid tag and vice versa.

The constraint is that the target post's file must exist in `_posts/` at build time. If the target is staged forward in time, the link is fine. If the target has not yet been published into `_posts/`, the build will fail with `could not find post_url`.

## Visibility Considerations

The human pilot has noted that the chronological-position behaviour is acceptable for forward-dated work. The article is technically visible at its URL on deploy, but the chronological position keeps it out of the way for any reader browsing the homepage or feed until the date arrives.

If true invisibility until the future date is required, switch `future: false` on the relevant deploy. This is a global setting and would affect every forward-dated post on the site, so it is not the default operating mode. The series cadence assumes `future: true`.

## Series Application

- Forward-dated series at one article per day: use the incremental publication pattern from [Cross-Linked Series](./CROSS_LINKED_SERIES.md).
- Back-dated series filling a calendar gap: use the batch publication pattern from [Cross-Linked Series](./CROSS_LINKED_SERIES.md). The articles deploy at their past positions immediately.

Two independent series can run in parallel if their date ranges do not collide. The analog-facilities forward-dated series and the patents-and-startup back-dated series ran in parallel without conflict because their date ranges were disjoint.

## Related Sections

- [Cross-Linked Series](./CROSS_LINKED_SERIES.md) for series-level publication patterns
- [Content Workflow](./CONTENT_WORKFLOW.md) for the per-article publication flow
- [Jekyll Structure](../architecture/JEKYLL_STRUCTURE.md) for site configuration
