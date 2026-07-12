# frozen_string_literal: true

# Computes corpus statistics and exposes them via site.data.stats so the
# /stats/ page can render them without fighting Liquid's limitations
# around sorting hashes by value.

module Jekyll
  class StatsGenerator < Generator
    safe true
    priority :low

    def generate(site)
      posts = site.posts.docs

      # Word count per post plus total
      word_counts = {}
      total_words = 0
      posts.each do |post|
        # Strip liquid tags before counting to avoid double-counting
        # template scaffolding. Kramdown output is close enough to plain
        # text for word counting purposes.
        content = post.content.to_s.gsub(/\{%[^%]*%\}/, "").gsub(/<[^>]*>/, "")
        count = content.split(/\s+/).size
        word_counts[post.url] = count
        total_words += count
      end

      # Top categories by post count
      category_counts = {}
      site.categories.each do |name, cat_posts|
        category_counts[name] = cat_posts.size
      end
      top_categories = category_counts.sort_by { |_n, c| -c }.first(20).map do |name, count|
        { "name" => name, "count" => count }
      end

      # Longest posts by word count
      longest_posts = word_counts.sort_by { |_url, c| -c }.first(15).map do |url, count|
        post = posts.find { |p| p.url == url }
        {
          "url" => url,
          "title" => post ? post.data["title"] : "",
          "date" => post ? post.data["date"] : nil,
          "word_count" => count
        }
      end

      # Posts per month for a longer-term timeline
      months = Hash.new(0)
      posts.each do |post|
        key = post.data["date"].strftime("%Y-%m")
        months[key] += 1
      end
      months_sorted = months.sort.map do |key, count|
        { "month" => key, "count" => count }
      end

      # Expose via site.data.stats
      site.data["stats"] = {
        "total_posts" => posts.size,
        "total_words" => total_words,
        "total_categories" => site.categories.size,
        "total_tags" => site.tags.size,
        "top_categories" => top_categories,
        "longest_posts" => longest_posts,
        "months" => months_sorted,
        "average_words_per_post" => posts.size.zero? ? 0 : (total_words / posts.size)
      }
    end
  end
end
