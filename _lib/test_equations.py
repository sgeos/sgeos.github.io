"""Regression cases for candidate preview, migration layout and Notation escaping.

These tests need no network or scratch fixtures.
"""
import contextlib
import copy
import io
from pathlib import Path
import tempfile
import unittest

import equations as E


class EquationWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.text = '---\nmathjax: true\n---\n<!-- A999 -->\n\nProse.\n\n$$x = 1$$\n\n## References\n\n'
        self.data = {'caution': 'Use consistent units.', 'equation': [
            {'tag': 1, 'class': 'standard', 'title': 'Identity',
             'gloss': 'The value is fixed.', 'digest': E.digest('x = 1')}]}

    def generated(self, text=None):
        return E.written(E.tagged(E.unfolded(text or self.text)), self.data)

    def test_preview_valid_and_stale(self):
        self.assertIn('Equation 1', E.preview(self.text, self.data))
        stale = copy.deepcopy(self.data)
        stale['equation'][0]['digest'] = 'wrong'
        with self.assertRaises(E.EquationError):
            E.preview(self.text, stale)
        with self.assertRaises(E.EquationError):
            E.preview(self.text, {})

    def test_preview_cli_never_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            post = Path(directory) / 'post.md'
            data = Path(directory) / 'candidate.toml'
            post.write_text(self.text)
            data.write_text('caution = "Use consistent units."\n[[equation]]\ntag = 1\nclass = "standard"\n'
                            'title = "Identity"\ngloss = "The value is fixed."\ndigest = "'
                            + E.digest('x = 1') + '"\n')
            original = (post.read_bytes(), data.read_bytes())
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(E.main(['equations', 'preview', str(post), str(data), '--show']), 0)
            self.assertIn('Equation 1', output.getvalue())
            self.assertEqual(original, (post.read_bytes(), data.read_bytes()))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(E.main(['equations', 'preview', str(post), str(data), '--write']), 2)
                data.write_text('not valid toml !!!')
                invalid = data.read_bytes()
                self.assertEqual(E.main(['equations', 'preview', str(post), str(data)]), 1)
            self.assertEqual(post.read_bytes(), original[0])
            self.assertEqual(data.read_bytes(), invalid)

    def test_audit_allows_generation_tags_and_separation(self):
        E.audit(self.text, self.generated())
        adjacent = self.text.replace('Prose.\n\n$$', 'Prose.\n$$')
        E.audit(adjacent, self.generated())
        retagged = self.generated().replace('\\tag{1}', '\\tag{7}')
        E.audit(self.generated(), retagged)

    def test_audit_rejects_nonlayout_changes(self):
        after = self.generated()
        for old, new in [('Prose.', 'Changed.'), ('x = 1', 'x = 2'),
                         ('mathjax: true', 'mathjax: false'),
                         ('## References\n\n', '## References\n\n[ref]: https://example.org\n')]:
            with self.subTest(old=old), self.assertRaises(E.EquationError):
                E.audit(self.text, after.replace(old, new))
        with self.assertRaises(E.EquationError):
            E.audit(self.text, self.text)
        with self.assertRaises(E.EquationError):
            E.audit(self.text, after.replace('$$', '$', 1))

    def test_audit_preserves_tag_lines_outside_math(self):
        for extra in ['\\tag{5}\n', '```tex\n\\tag{5}\n```\n']:
            before = self.text.replace('Prose.\n', 'Prose.\n' + extra)
            after = self.generated(before)
            E.audit(before, after)
            with self.assertRaises(E.EquationError):
                E.audit(before, after.replace('\\tag{5}', '\\tag{6}'))

    def test_cli_audit_and_input_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            before = Path(directory) / 'before.md'
            after = Path(directory) / 'after.md'
            before.write_text(self.text)
            after.write_text(self.generated())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(E.main(['equations', 'audit', str(before), str(after)]), 0)
                self.assertEqual(E.main(['equations', 'audit', str(before)]), 2)
                self.assertEqual(E.main(['equations', 'preview', str(before), 'missing-file']), 1)
                self.assertEqual(E.main(['equations', 'audit', str(before), 'missing-file']), 1)
            after.write_text(self.generated().replace('Prose.', 'Changed.'))
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(E.main(['equations', 'audit', str(before), str(after)]), 1)
            self.assertIn(f'{before} -> {after}', output.getvalue())

    def test_notation_cross_span_underscores_and_stars(self):
        row = E.notation_row(r'\dot{m}_{0}', r'the flow, with $\dot{m}_{e}$ the exit flow')
        self.assertIn(r'\dot{m}\_{0}', row)
        self.assertIn(r'\dot{m}\_{e}', row)
        self.assertEqual(E.notation_row('I^{*}', 'the investment, with $S^{*}$ the surplus'),
                         r'- $I^{\*}$, the investment, with $S^{\*}$ the surplus')
        self.assertEqual(E.notation_row('x', r'the value, with $\dot{m}_c$ and $\dot{m}_{gg}$ flows'),
                         r'- $x$, the value, with $\dot{m}\_c$ and $\dot{m}\_{gg}$ flows')
        self.assertEqual(E.notation_row('x^2_i', 'the square, with $y_{j}$ the other'),
                         r'- $x^2\_i$, the square, with $y\_{j}$ the other')
        self.assertEqual(E.notation_row('x', r'the value $\dot{m}_{a} + \dot{m}_{b}$'),
                         r'- $x$, the value $\dot{m}\_{a} + \dot{m}\_{b}$')

    def test_notation_preserves_prose_code_and_safe_math(self):
        for tex, meaning in [('x_i', 'the value'), ('x', 'plain *emphasis* and `a_b * c`'),
                             (r'\dot{m}_c', r'the flow with $\dot{m}_h$'),
                             (r'\dot{m}\_{0}', r'the flow with $\dot{m}\_{e}$')]:
            self.assertEqual(E.notation_row(tex, meaning), f'- ${tex}$, {meaning}')
        row = E.notation_row('I^{*}', 'the *investment*, with $S^{*}$ and `x*y`')
        self.assertIn('the *investment*', row)
        self.assertIn('`x*y`', row)
        self.assertEqual(E.notation_row('a-_i', 'the value, with $b_{j}$'),
                         '- $a-_i$, the value, with $b_{j}$')


if __name__ == '__main__':
    unittest.main()
