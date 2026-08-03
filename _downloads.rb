#!/usr/bin/env ruby
# frozen_string_literal: true

# Generates PDF and EPUB downloads for every published post and writes them
# into the built site directory alongside each post's HTML output. Runs after
# `jekyll build` in CI. Skips gracefully with a warning if pandoc is not
# installed, so local previews without pandoc still succeed.

require 'yaml'
require 'fileutils'
require 'tempfile'
require 'date'

POSTS_DIR   = File.expand_path('_posts', __dir__)
SITE_DIR    = File.expand_path('_site',  __dir__)
SITE_URL    = 'https://sgeos.github.io'
DEFAULT_AUTHOR = 'Brendan Sechter'

def have?(cmd)
  system("command -v #{cmd} >/dev/null 2>&1")
end

unless have?('pandoc')
  warn '[_downloads.rb] pandoc not installed; skipping PDF/EPUB generation.'
  exit 0
end

have_xelatex = have?('xelatex')
warn '[_downloads.rb] xelatex not installed; PDF generation will be skipped.' unless have_xelatex

def parse_front_matter(content)
  m = content.match(/\A---\s*\n(.*?)\n---\s*\n(.*)/m)
  return [nil, content] unless m
  fm = YAML.safe_load(m[1], permitted_classes: [Time, Date])
  [fm, m[2]]
end

def slug_and_date(basename)
  m = basename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+)$/)
  return nil unless m
  { year: m[1], month: m[2], day: m[3], slug: m[4] }
end

def categories_of(fm)
  cats = fm['categories']
  cats = cats.split if cats.is_a?(String)
  cats || []
end

# Locate the HTML Jekyll actually emitted for this post, rather than
# reconstructing the path from the source filename.
#
# The filename date and the front matter `date:` are not always the same, and
# even when they agree Jekyll derives the permalink from the front matter date
# converted to the build machine's timezone. Nineteen posts in this corpus
# resolve to a different day than their filename implies, sixteen of them 2016
# posts stamped +0900 in the early morning. Reconstructing the path wrote their
# EPUB into a directory with no matching HTML, producing a 404 download link on
# the post page and an orphan file in the artifact.
#
# Globbing the built site sidesteps date arithmetic and timezone configuration
# entirely: whatever Jekyll produced is the truth.
def find_permalink(fm, slug)
  cats = categories_of(fm)
  pattern = File.join(SITE_DIR, *cats, '*', '*', '*', "#{slug}.html")
  matches = Dir.glob(pattern)
  return nil unless matches.size == 1
  "/#{matches.first.sub(%r{\A#{Regexp.escape(SITE_DIR)}/}, '')}"
end

# Build post_url resolution map keyed by source basename (without extension).
url_map = {}
permalinks = {}
Dir.glob(File.join(POSTS_DIR, '*.markdown')).each do |path|
  basename = File.basename(path, '.markdown')
  fm, _ = parse_front_matter(File.read(path))
  next unless fm
  info = slug_and_date(basename)
  next unless info
  permalink = find_permalink(fm, info[:slug])
  next unless permalink
  permalinks[basename] = permalink
  url_map[basename] = "#{SITE_URL}#{permalink}"
end

def preprocess(body, url_map)
  # Resolve {% post_url basename %} to absolute site URLs so cross-links
  # work when read offline. Unknown targets become '#'.
  body = body.gsub(/\{%\s*post_url\s+([\w-]+)\s*%\}/) do
    url_map[$1] || '#'
  end
  # Strip remaining Liquid statements and expressions.
  body = body.gsub(/\{%[\s\S]*?%\}/, '')
  body = body.gsub(/\{\{[\s\S]*?\}\}/, '')
  # Strip inline debug scripts and HTML comments.
  body = body.gsub(/<script[\s\S]*?<\/script>/i, '')
  body = body.gsub(/<!--[\s\S]*?-->/, '')
  body.strip
end

pdf_ok = 0
epub_ok = 0
skipped = 0
failed  = []

Dir.glob(File.join(POSTS_DIR, '*.markdown')).sort.each do |path|
  basename = File.basename(path, '.markdown')
  fm, raw_body = parse_front_matter(File.read(path))
  unless fm && url_map[basename]
    skipped += 1
    next
  end
  info = slug_and_date(basename)

  permalink = permalinks[basename]
  out_dir = File.join(SITE_DIR, File.dirname(permalink))
  slug = info[:slug]
  pdf_out  = File.join(out_dir, "#{slug}.pdf")
  epub_out = File.join(out_dir, "#{slug}.epub")

  unless Dir.exist?(out_dir)
    # The directory came from a file Jekyll emitted, so this should be
    # unreachable. Skip rather than guess if it ever is not.
    skipped += 1
    next
  end

  body = preprocess(raw_body, url_map)
  title = fm['title'].to_s
  date  = fm['date'] ? fm['date'].to_s.split(/[ T]/).first : ''

  tmp = Tempfile.new(['post', '.md'])
  begin
    tmp.write(body)
    tmp.close

    reader = 'markdown+tex_math_dollars+tex_math_single_backslash+tex_math_double_backslash+raw_html'
    common_meta = [
      '--metadata', "title=#{title}",
      '--metadata', "author=#{DEFAULT_AUTHOR}",
      '--metadata', "date=#{date}",
    ]

    if have_xelatex
      pdf_cmd = ['pandoc', tmp.path,
                 '--from', reader,
                 '--standalone',
                 '--pdf-engine=xelatex',
                 '-V', 'mainfont=DejaVu Serif',
                 '-V', 'monofont=DejaVu Sans Mono',
                 '-V', 'CJKmainfont=Noto Sans CJK JP',
                 '-V', 'geometry:margin=1in',
                 '-V', 'colorlinks=true',
                 '-V', 'linkcolor=RoyalBlue',
                 '-V', 'urlcolor=RoyalBlue',
                 *common_meta,
                 '-o', pdf_out]
      if system(*pdf_cmd)
        pdf_ok += 1
      else
        failed << "#{basename} (pdf)"
      end
    end

    epub_cmd = ['pandoc', tmp.path,
                '--from', reader,
                '--to', 'epub',
                '--standalone',
                '--mathml',
                *common_meta,
                '-o', epub_out]
    if system(*epub_cmd)
      epub_ok += 1
    else
      failed << "#{basename} (epub)"
    end
  ensure
    tmp.unlink
  end
end

puts "[_downloads.rb] pdf=#{pdf_ok} epub=#{epub_ok} skipped=#{skipped} failed=#{failed.size}"
unless failed.empty?
  warn "[_downloads.rb] failures: #{failed.join(', ')}"
end

# Fail the build on SYSTEMIC failure, meaning a format was attempted for every
# post and produced nothing at all. That is a broken toolchain, not a bad post.
#
# This script previously only warned. A missing `lmodern.sty` made every single
# PDF fail while the workflow step still reported success, so roughly 293 posts
# linked a PDF that had never existed and nothing surfaced it. An exit code is
# the only signal CI reads.
#
# Individual failures still only warn, so one malformed post cannot block a
# deploy.
attempted = pdf_ok + epub_ok + failed.size
if attempted.positive?
  systemic = []
  systemic << 'PDF' if have_xelatex && pdf_ok.zero?
  systemic << 'EPUB' if epub_ok.zero?
  unless systemic.empty?
    warn "[_downloads.rb] SYSTEMIC FAILURE: #{systemic.join(' and ')} generation produced zero outputs."
    warn '[_downloads.rb] This indicates a broken toolchain rather than bad content. Failing the build.'
    exit 1
  end
end
