# frozen_string_literal: true

# Generates a reverse index of post_url references across the corpus and
# attaches the result to each post as `page.backlinks`.
#
# The corpus uses `{% post_url YYYY-MM-DD-slug %}` liquid tags to
# cross-reference other posts. That reference is one-way. This generator
# walks every post, extracts every post_url reference, and builds a map
# from target post URL to the list of posts that link to it. The map is
# attached to each post's data so the post layout can render a
# "Referenced by" section.

module Jekyll
  class BacklinksGenerator < Generator
    safe true
    priority :low

    POST_URL_PATTERN = /\{%\s*post_url\s+([^\s%]+)\s*%\}/

    def generate(site)
      # Build lookup: slug (basename without ext) -> Document
      slug_to_post = {}
      site.posts.docs.each do |post|
        slug = post.basename_without_ext
        slug_to_post[slug] = post
      end

      # Walk each post, collect references
      backlinks = Hash.new { |h, k| h[k] = [] }
      site.posts.docs.each do |post|
        content = post.content.to_s
        content.scan(POST_URL_PATTERN) do |match|
          target_slug = match[0]
          target = slug_to_post[target_slug]
          next unless target
          next if target.url == post.url # avoid self-links

          backlinks[target.url] << {
            "url" => post.url,
            "title" => post.data["title"],
            "date" => post.data["date"]
          }
        end
      end

      # Attach to each post's data; sort by date descending
      site.posts.docs.each do |post|
        entries = backlinks[post.url] || []
        entries = entries.uniq { |e| e["url"] }
        entries = entries.sort_by { |e| e["date"] }.reverse
        post.data["backlinks"] = entries
      end
    end
  end
end
