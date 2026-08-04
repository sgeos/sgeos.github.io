# Cross-Linked Series Publication

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

A series whose articles cross-link one another with `{% post_url %}` Liquid tags has two valid publication patterns. The pattern selected affects the build, the deploy, and the order of commits.

## Incremental Publication

Publish one article per day. Each article may resolve a `{% post_url %}` tag only to articles already in `_posts/`. Forward references to later, unpublished articles must be prose only, with no Liquid tag.

This pattern fits a series authored over time, where each article is finalised and reviewed before the next begins. The analog-facilities series at A152 through A160 used this cadence, with each article published the day after the previous.

Workflow per article:
- Draft and review the article.
- Stage and commit in `_drafts/`.
- Move to `_posts/` with `git mv` and commit.
- Push to deploy through GitHub Actions.

The next article in the series may now reference this one via `{% post_url %}` because the target file exists in `_posts/`.

## Batch Publication

Stage every article of the series into `_posts/` together, at which point all internal
`{% post_url %}` tags resolve at once, including forward references between articles in the
series.

**This holds only when every article in the batch is back-dated.** The site sets `future: false`,
so a forward-dated article is excluded from the build even though its file sits in `_posts/`.
Staging the batch together does not help if part of it is dated ahead: a reference from an
included article to an excluded one fails the entire build. See
[Forward-Dated Posts](./FORWARD_DATED_POSTS.md).

The three safe configurations are:

- **All dates passed.** Every article is in the build and every internal tag resolves. This is
  the case the batch pattern is designed for.
- **All dates in the future.** Every article is excluded together, so no internal tag is
  evaluated. The whole cluster becomes eligible as its dates arrive.
- **Mixed dates with back-reference-only.** Articles whose dates have passed may reference each
  other, and nothing points forward at an article still excluded.

This pattern fits a tightly cross-linked set authored in advance, where forward references are
unavoidable. The patents-and-startup series at A161 through A172 used this batch pattern, and it
worked because that series was back-dated in full.

Workflow for the batch:
- Confirm article numbers, dates, and slugs across the full batch.
- Verify cross-link integrity: every `{% post_url YYYY-MM-DD-slug %}` references a destination that will exist after the move.
- Stage all drafts to track them. Commit as `_drafts/`.
- Move all files to `_posts/` in a single batch with `git mv`. Commit and push.

Stage the whole series before the deploy build, not one article at a time, or the build fails on the unresolved forward tags. A drafts-only preview likewise fails on the unresolved tags until the batch is staged, which is expected.

## Choosing the Pattern

| Pattern | Use when |
|---------|----------|
| Incremental | Series authored over time; review cycle between articles; no forward cross-references at publication time |
| Batch | Series authored in advance; cross-links span the full series; back-dated to fill a calendar gap |

Both patterns produce identical deployed content. The choice is operational, not editorial.

## Build Verification

Both patterns require the GitHub Actions deploy build to resolve every `{% post_url %}` tag. A `could not find post_url` error in the build log indicates a typo in a slug or a forward reference that should have been prose-only under the incremental pattern.

Build locally the way CI does. The bundle was long believed broken on macOS; it was simply never
installed. `bundle install` succeeds, native extensions and all.

```sh
bundle install                      # one time, installs into vendor/bundle (gitignored)
JEKYLL_ENV=production bundle exec jekyll build --baseurl ""
```

That reproduces the deploy closely: the same Jekyll 4.4.1 from `Gemfile.lock`, the same production
environment, and `jekyll-archives` active so category and tag pages are generated. Measured against
the live sitemap it produces 451 pages to the live site's 450 URLs, the difference being two asset
PDFs the sitemap lists and three pages carrying `sitemap: false`.

**Do not use a Gemfile-free build with `jekyll-archives` stripped.** That was the earlier workaround
and it is actively misleading. A link crawl of such a build reported 740 broken targets, every one
of them fine in production, because the archive pages it links to were never generated. Worse, it
cannot see the class of defect that a faithful build finds: on 2026-08-05 the faithful build
surfaced two genuinely broken category links live on the site, `/categories/c++/` and
`/categories/no_std/`, where the templates emitted the raw category while `jekyll-archives`
slugifies it.

Two steps still require tooling CI installs and a workstation may not have. Both degrade
gracefully, so their absence shows up only as missing `.pdf` and `.epub` links and a missing
`/pagefind/` directory in a crawl:

```sh
ruby _downloads.rb                  # needs pandoc, texlive-xetex, lmodern, texlive-lang-chinese
npx -y pagefind --site _site        # needs node
```

`_downloads.rb` reads and writes `_site`, so run the build without `--destination` if you want it.

Watch the GitHub Actions log on the push commit as confirmation, not as the primary check.

## Related Sections

- [Content Workflow](./CONTENT_WORKFLOW.md) for the per-article publication flow
- [Forward-Dated Posts](./FORWARD_DATED_POSTS.md) for the `future: false` configuration that withholds future-dated posts until their dates arrive
- [Git Strategy](./GIT_STRATEGY.md) for commit conventions
