source "https://rubygems.org"

# Modern Jekyll for the GitHub Actions build. The github-pages gem is
# intentionally NOT used. It pins old, vulnerable transitive dependencies
# (nokogiri and friends) to mirror the stock GitHub Pages branch build, and
# it does not let those be bumped. Because this site deploys through a
# custom GitHub Actions build instead, it can run current, patched
# dependencies and still honor the _plugins Rouge lexer that highlights
# Keleusma code.
gem "jekyll", "~> 4.3"

# Pin the highlighter to the version the Keleusma _plugins lexer is tested
# against, and keep the libsass-based Sass converter that compiles this
# site's existing SCSS. Both are the versions verified to build the site
# with correct Keleusma highlighting.
gem "rouge", "~> 3.30"
gem "jekyll-sass-converter", "~> 2.0"

# Plugins the stock github-pages build used to auto-enable. Only the ones
# that produce artifacts this site relies on are kept.
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"     # generates /feed.xml (linked from the index)
  gem "jekyll-sitemap", "~> 1.4"   # generates /sitemap.xml
end

# Required for `jekyll serve` on Ruby 3.x.
gem "webrick", "~> 1.8"
