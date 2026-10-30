# frozen_string_literal: true

# Rewrites a post's Markdown so that pandoc reads its mathematics the way the
# site does. Used by `_downloads.rb` before the PDF and EPUB conversions.
#
# WHY THIS EXISTS. The site's mathematics passes through two programs, kramdown
# and then MathJax, and pandoc imitates neither exactly. Every rule below
# matches a divergence that failed a PDF build in October 2026, when 94 of 384
# posts had no PDF. The rules make pandoc agree with what a reader of the page
# already sees. None of them changes what the site renders.
#
# Trust boundary. The input is a post from this repository, and the output only
# reaches pandoc as a file. Nothing is evaluated.
module PandocInput
  module_function

  # Liquid renders `{{2}}` as `2` on the site, so `V^{{2}}` reaches MathJax as
  # `V^2`. The generic Liquid strip in `_downloads.rb` removed the number
  # instead, which left a dangling superscript, and XeLaTeX stopped with
  # "Double subscript". Only a bare numeric literal is resolved. Any other
  # expression is left for the generic strip.
  def liquid_numbers(body)
    body.gsub(/\{\{\s*(-?\d+(?:\.\d+)?)\s*\}\}/) { Regexp.last_match(1) }
  end

  # Single-dollar inline mathematics, normalised to what MathJax receives.
  #
  # Kramdown does not treat `$x$` as mathematics, so it applies its backslash
  # escapes inside it. `$\pi^\*$` therefore reaches MathJax as `$\pi^*$`.
  # Pandoc keeps `\*`, which XeLaTeX reads as a discretionary times sign and
  # rejects in a superscript. That failed 20 posts. `\_` is unescaped for the
  # same reason.
  #
  # MathJax also accepts `$ B $`. Pandoc's tex_math_dollars does not, because an
  # opening dollar must be followed by a non-space and a closing one preceded by
  # one, so it passed `\left` and subscripts to LaTeX as text. That failed 3
  # posts. The whitespace just inside each delimiter is removed.
  #
  # Delimiters are paired left to right within one line, as MathJax pairs them.
  # A line is left untouched when its dollar count is odd, because the pairing
  # is then ambiguous. Fenced code, indented code, inline code spans and display
  # blocks are never altered, and `\$` and `$$` are not delimiters here.
  def inline_math(body)
    fence = nil
    display = false
    body.lines.map do |line|
      stripped = line.strip
      if fence
        fence = nil if stripped.start_with?(fence)
        next line
      end
      if (m = stripped.match(/\A(`{3,}|~{3,})/))
        fence = m[1]
        next line
      end
      if line.include?('$$')
        display = !display if line.scan('$$').size.odd?
        next line
      end
      next line if display || line.match?(/\A(?: {4}|\t)/)

      inline_math_line(line)
    end.join
  end

  # One line of prose. Code spans are masked so a dollar inside one is neither
  # counted nor changed.
  def inline_math_line(line)
    spans = []
    masked = line.gsub(/(`+).*?\1/) do |code|
      spans << code
      "\u0000#{spans.size - 1}\u0000"
    end
    marks = []
    masked.to_enum(:scan, /(?<![\\$])\$(?!\$)/).each { marks << Regexp.last_match.begin(0) }
    return line if marks.empty? || marks.size.odd?

    out = +''
    cursor = 0
    marks.each_slice(2) do |open, close|
      out << masked[cursor...open] << '$' << inline_math_content(masked[(open + 1)...close], masked[close + 1])
      out << '$'
      cursor = close + 1
    end
    out << masked[cursor..]
    out.gsub(/\u0000(\d+)\u0000/) { spans[Regexp.last_match(1).to_i] }
  end

  # The text between one pair of dollars, rewritten only where it is plainly TeX.
  #
  # A pair of dollars on one line is also how two prices look, as in "$400 to
  # $5,000", and pandoc rightly reads that as text. So the whitespace is removed
  # only when the content carries a TeX character or an equals sign, or is a
  # single letter, does not open with a digit,
  # and the closing dollar is not followed by one. The escapes are resolved
  # under the same test. Otherwise the content is returned unchanged.
  def inline_math_content(inner, after)
    texlike = inner.match?(/[\\^_{=]/) || inner.strip.match?(/\A[A-Za-z]\z/)
    tex = texlike && !inner.lstrip.match?(/\A\d/) && !after.to_s.match?(/\d/)
    return inner unless tex

    inner.strip.gsub('\\*', '*').gsub('\\_', '_')
  end
end
