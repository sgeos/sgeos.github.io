# frozen_string_literal: true

# Computes related posts for each post by category overlap and attaches
# the result to page.related_posts. Unlike Jekyll's built-in
# site.related_posts which uses either latest or LSI-based semantic
# similarity, this generator ranks by number of shared categories then
# by publication date descending.
#
# Backlinks (from _plugins/backlinks.rb) show posts that explicitly
# reference this one via post_url tags. This generator shows posts that
# cover the same topics whether or not they reference each other.

module Jekyll
  class RelatedPostsGenerator < Generator
    safe true
    priority :low

    LIMIT = 5

    def generate(site)
      posts = site.posts.docs

      posts.each do |post|
        post_categories = Array(post.data["categories"]).map(&:to_s)
        next if post_categories.empty?
        post_cat_set = post_categories.to_set

        candidates = posts.reject { |p| p.url == post.url }
        candidates = candidates.map do |candidate|
          cand_cats = Array(candidate.data["categories"]).map(&:to_s).to_set
          overlap = (post_cat_set & cand_cats).size
          [candidate, overlap]
        end
        candidates = candidates.reject { |_p, overlap| overlap.zero? }

        # Sort by descending overlap, then descending date
        candidates = candidates.sort_by do |candidate, overlap|
          [-overlap, -candidate.data["date"].to_i]
        end

        related = candidates.first(LIMIT).map do |candidate, overlap|
          {
            "url" => candidate.url,
            "title" => candidate.data["title"],
            "date" => candidate.data["date"],
            "overlap" => overlap,
            "categories" => Array(candidate.data["categories"]).map(&:to_s)
          }
        end

        post.data["related_posts"] = related
      end
    end
  end
end

# Require Set for Ruby versions before 3.2 where Set is auto-loaded.
require "set"
