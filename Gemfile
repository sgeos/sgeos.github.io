source "https://rubygems.org"

# Use the github-pages gem so local builds, the legacy branch build, and
# the GitHub Actions build all resolve the same Jekyll, Kramdown, and Rouge
# versions GitHub Pages uses. The Actions build (unlike the stock branch
# build) does not run Jekyll in safe mode, so the custom Rouge lexer in
# `_plugins/keleusma_lexer.rb` is honored and `keleusma` code fences are
# highlighted on the deployed site.
gem "github-pages", group: :jekyll_plugins

# Required for `jekyll serve` on Ruby 3.x.
gem "webrick"
