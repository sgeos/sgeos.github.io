# Vendored from the Keleusma repository: editors/rouge/keleusma.rb
# Source of truth lives there; keep this copy in sync on Keleusma grammar changes.
#
# frozen_string_literal: true

# Rouge lexer for the Keleusma scripting language.
#
# Keleusma is a total functional stream-processing language. This lexer
# emits standard Rouge token types so that any existing Rouge theme
# styles Keleusma source without bespoke CSS. Token coverage mirrors the
# TextMate grammar in editors/vscode/syntaxes/keleusma.tmLanguage.json.
#
# Usage with Jekyll: copy this file into the site's `_plugins/` directory
# (a non-safe build is required, for example a GitHub Actions build, since
# the stock GitHub Pages branch build runs Jekyll in safe mode and ignores
# plugins). Then fence Keleusma code with ```keleusma.
#
# Usage with rougify: `rougify highlight file.kel -r ./keleusma.rb -l keleusma`.

require 'rouge'

module Rouge
  module Lexers
    class Keleusma < RegexLexer
      title 'Keleusma'
      desc 'The Keleusma total functional stream-processing language'
      tag 'keleusma'
      aliases 'kel'
      filenames '*.kel'
      mimetypes 'text/x-keleusma'

      # Function-category keywords. The category drives every verifier
      # rule, so it is highlighted distinctly from storage and keywords.
      def self.declarations
        @declarations ||= Set.new %w(fn yield loop)
      end

      # Storage-discipline modifiers, a separate category from the
      # function-category keywords per the shared categorisation scheme.
      def self.storage
        @storage ||= Set.new %w(signed ephemeral shared private const)
      end

      # Information-flow operators. Grouped with the @-label annotations
      # so the whole IFC surface shares one highlight category.
      def self.ifc_operators
        @ifc_operators ||= Set.new %w(classify declassify)
      end

      # Control-flow and other reserved words.
      def self.keywords
        @keywords ||= Set.new %w(
          if else match when for break
          let in use external struct enum newtype trait impl data pure where as
        )
      end

      # Word-spelled operators.
      def self.word_operators
        @word_operators ||= Set.new %w(and or not)
      end

      # Primitive value types. `i64` is the integer-literal suffix and the
      # V0.1.x integer type name, retained so legacy scripts highlight.
      def self.builtin_types
        @builtin_types ||= Set.new %w(Byte Word Fixed Float bool Text Option i64)
      end

      # Checked-arithmetic match arms.
      def self.builtins
        @builtins ||= Set.new %w(ok overflow underflow saturate_max saturate_min)
      end

      # Boolean literals.
      def self.constants
        @constants ||= Set.new %w(true false)
      end

      state :root do
        rule %r/\A#!.*$/, Comment::Single
        rule %r(//.*?$), Comment::Single
        rule %r(/\*), Comment::Multiline, :comment
        rule %r/\s+/, Text::Whitespace
        rule %r/"/, Str::Double, :string

        # Information-flow labels: @Label, @!Label, @{set}.
        rule %r/@!?(?:[A-Za-z_]\w*|\{[^}]*\})/, Name::Decorator

        # Numeric literals. Float, hex, and binary precede integer.
        rule %r/\b\d[0-9_]*\.\d[0-9_]*(?:f64)?\b/, Num::Float
        rule %r/\b0x[0-9a-fA-F_]+\b/, Num::Hex
        rule %r/\b0b[01_]+\b/, Num::Bin
        rule %r/\b\d[0-9_]*(?:i64)?\b/, Num::Integer

        # Identifier-shaped tokens routed by keyword class.
        rule %r/[a-z_]\w*/ do |m|
          name = m[0]
          if self.class.word_operators.include?(name)
            token Operator::Word
          elsif self.class.declarations.include?(name)
            token Keyword::Declaration
          elsif self.class.storage.include?(name)
            token Keyword::Reserved
          elsif self.class.ifc_operators.include?(name)
            token Name::Decorator
          elsif self.class.keywords.include?(name)
            token Keyword
          elsif self.class.constants.include?(name)
            token Keyword::Constant
          elsif self.class.builtin_types.include?(name)
            token Keyword::Type
          elsif self.class.builtins.include?(name)
            token Name::Builtin
          else
            token Name
          end
        end

        # Capitalized names. Primitive types are highlighted as types,
        # everything else capitalized as a class or variant name.
        rule %r/[A-Z]\w*/ do |m|
          if self.class.builtin_types.include?(m[0])
            token Keyword::Type
          else
            token Name::Class
          end
        end

        # Operators. Multi-character forms precede their prefixes.
        rule %r/\|>/, Operator
        rule %r/->|=>/, Operator
        rule %r/::/, Operator
        rule %r/\.\./, Operator
        rule %r/<<|>>/, Operator
        rule %r/==|!=|<=|>=/, Operator
        rule %r/[+\-*\/%<>=&|\^!]/, Operator

        rule %r/[()\[\]{},;:.]/, Punctuation
      end

      state :comment do
        rule %r([^*\/]+), Comment::Multiline
        rule %r(/\*), Comment::Multiline, :comment
        rule %r(\*/), Comment::Multiline, :pop!
        rule %r([*\/]), Comment::Multiline
      end

      state :string do
        rule %r/[^"\\]+/, Str::Double
        rule %r/\\[ntr"\\0]/, Str::Escape
        rule %r/\\./, Str::Escape
        rule %r/"/, Str::Double, :pop!
      end
    end
  end
end
