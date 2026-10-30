# frozen_string_literal: true

# Regression tests for `_lib/pandoc_input.rb`. Each positive case is a form that
# failed a PDF build in October 2026, and each negative case is text the rewrite
# must leave alone. Run with `ruby _lib/test_pandoc_input.rb`.

require 'minitest/autorun'
require_relative 'pandoc_input'

class TestLiquidNumbers < Minitest::Test
  def test_numeric_literal_renders_as_the_number
    assert_equal 'V^2 C', PandocInput.liquid_numbers('V^{{2}} C')
    assert_equal 'x^ -1.5', PandocInput.liquid_numbers('x^ {{ -1.5 }}')
  end

  def test_other_expressions_are_left_for_the_generic_strip
    assert_equal '{{ post.url }}', PandocInput.liquid_numbers('{{ post.url }}')
  end
end

class TestInlineMath < Minitest::Test
  def rewrite(text) = PandocInput.inline_math(text)

  def test_escaped_star_and_underscore_are_unescaped_inside_math
    assert_equal "An optimal policy $\\pi^*$ and $\\mathcal{A}_{\\phi^*}$.\n",
                 rewrite("An optimal policy $\\pi^\\*$ and $\\mathcal{A}\\_{\\phi^\\*}$.\n")
  end

  def test_whitespace_inside_delimiters_is_removed
    assert_equal "condition $B \\left( K \\right) = A$ is solved\n",
                 rewrite("condition $ B \\left( K \\right) = A $ is solved\n")
  end

  def test_pairs_are_taken_left_to_right
    assert_equal "Let $F$ be thrust, $\\dot{m}$ the flow\n", rewrite("Let $F$ be thrust, $\\dot{m}$ the flow\n")
  end

  def test_escapes_outside_math_are_untouched
    assert_equal "a \\* b and $x$ and c\\_d\n", rewrite("a \\* b and $x$ and c\\_d\n")
  end

  def test_prices_are_left_alone
    line = "| Batteries | $400 to $5,000 | $1,000 to $10,000 |\n"
    assert_equal line, rewrite(line)
    line = "fell from $26.12 on one date to $7.50 later\n"
    assert_equal line, rewrite(line)
  end

  def test_single_letters_and_equations_are_math
    assert_equal "between $a$ and $B X = Y$\n", rewrite("between $ a $ and $ B X = Y $\n")
  end

  def test_plain_word_content_is_left_alone
    line = "from $ five to $ ten\n"
    assert_equal line, rewrite(line)
  end

  def test_odd_dollar_count_leaves_the_line_alone
    line = "costs $5 and $ x $ here\n"
    assert_equal line, rewrite(line)
  end

  def test_escaped_dollar_is_not_a_delimiter
    line = "price \\$ 5 and $ y $\n"
    assert_equal "price \\$ 5 and $y$\n", rewrite(line)
  end

  def test_code_span_is_masked
    line = "run `echo $A $B` then $ z $\n"
    assert_equal "run `echo $A $B` then $z$\n", rewrite(line)
  end

  def test_fenced_and_indented_code_and_display_blocks_are_untouched
    text = "```sh\necho $ A $\n```\n    echo $ B $\n$$\nx^\\* $ y $\n$$\n$$ a \\_ b $$\n"
    assert_equal text, rewrite(text)
  end

  def test_tilde_fence_needs_a_matching_close
    text = "~~~\n``` not a close\n$ a $\n~~~\n$ b $\n"
    assert_equal "~~~\n``` not a close\n$ a $\n~~~\n$b$\n", rewrite(text)
  end
end
