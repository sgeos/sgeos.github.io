# Security Policy

## Supported versions

The live site at <https://sgeos.github.io> and the `master` branch that builds it are
supported. There are no releases.

## Reporting a vulnerability

Please report security issues privately, so that a fix can be prepared before public
disclosure. Open a draft advisory at
<https://github.com/sgeos/sgeos.github.io/security/advisories/new>. The maintainer is
notified and can work on the fix with you in the same place.

Please include the affected page or commit, a minimal way to reproduce the issue, the
expected and observed behaviour, and your assessment of severity if you have one.

## Response

The maintainer aims to acknowledge a report within a few days, and to either confirm the
issue or explain why it is not a vulnerability. Confirmed issues are fixed on `master`,
which deploys the site, on a disclosure timeline agreed with the reporter.

## Scope

In scope are the site as built and served, including its layouts, scripts, embedded
WebAssembly modules and comment integration, the build and deploy workflow, and the
tooling under `_lib/`. Out of scope are the accuracy of a post's content, which is a
correction to report as an ordinary issue, and the security of third-party services the
site links to or embeds, such as GitHub Pages and Giscus.
