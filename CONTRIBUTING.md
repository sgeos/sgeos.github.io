# Contributing

This is a personal blog, so most contributions are corrections. A factual error, a broken
link, a wrong citation or a rendering fault is worth reporting, and an issue is the
easiest way to report it. The issue templates ask for the post and the passage.

**Licensing.** The prose is dedicated to the public domain under CC0 1.0 Universal, and
the code, including code samples in posts, is licensed under 0BSD. By contributing you
agree that your contribution is released under the licence that covers what you changed.
Do not contribute material that you did not write, or that carries terms of its own.

Participation in the project's spaces follows the
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Contributions are judged on their merits.

## Before opening a pull request

1. Run `./_check.sh` and confirm that it exits zero. It runs the same corpus checks,
   production build and rendered audit as the deploy.
2. Keep each pull request to one change.
3. Write commit messages as scoped conventional commits, such as `fix:`, `docs:` or
   `feat:`, as [`_docs/process/GIT_STRATEGY.md`](_docs/process/GIT_STRATEGY.md) describes.
4. Do not weaken a check to make it pass. If a check is wrong, say so in the pull request
   and fix it deliberately.
5. Do not change a published post's date or categories without adding a redirect, since
   either moves its URL. [`CLAUDE.md`](CLAUDE.md) explains the redirect mechanism.

## Reporting security issues

Do not open a public issue for a vulnerability. Follow [`SECURITY.md`](SECURITY.md).
