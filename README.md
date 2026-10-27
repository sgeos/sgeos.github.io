# sgeos.github.io

[![Build and deploy](https://github.com/sgeos/sgeos.github.io/actions/workflows/jekyll.yml/badge.svg?branch=master)](https://github.com/sgeos/sgeos.github.io/actions/workflows/jekyll.yml)
[![Prose: CC0 1.0](https://img.shields.io/badge/prose-CC0%201.0-blue.svg)](LICENSE)
[![Code: 0BSD](https://img.shields.io/badge/code-0BSD-blue.svg)](LICENSE-0BSD)

The source of Brendan Sechter's technical blog at [sgeos.github.io](https://sgeos.github.io), a
Jekyll site built and deployed to GitHub Pages by GitHub Actions.

## Development

```sh
./_preview.sh            # serve the site locally at http://localhost:4000/
./_check.sh              # the deploy gate: corpus checks, a production build, the rendered audit
python3 _lib/blog.py     # the article and reference tooling, one command line
```

## Documentation

Agent guidance is in [`CLAUDE.md`](CLAUDE.md), and [`AGENTS.md`](AGENTS.md) points other
assistants to it. The documentation index is [`_docs/README.md`](_docs/README.md).
Contributions follow [`CONTRIBUTING.md`](CONTRIBUTING.md), participation follows the
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), and security reports follow
[`SECURITY.md`](SECURITY.md).

## License

The prose, meaning the posts, drafts, documentation and other writing and media, is
dedicated to the public domain under [CC0 1.0 Universal](LICENSE). The code, meaning the
site's layouts, styles, plugins, scripts and tooling and the code samples in posts, is
licensed under the [BSD Zero Clause License](LICENSE-0BSD). Neither requires attribution.
