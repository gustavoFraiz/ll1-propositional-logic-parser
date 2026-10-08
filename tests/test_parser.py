import unittest

from src.lexer import TokenType, tokenize
from src.parser import parse


class LexerTests(unittest.TestCase):
    def test_proposition(self):
        tokens = tokenize("1abc")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].token_type, TokenType.PROPOSICAO)

    def test_illegal_symbol(self):
        tokens = tokenize("@")
        self.assertEqual(tokens[0].token_type, TokenType.SIMBOLOILEGAL)


class ParserTests(unittest.TestCase):
    def assertValid(self, expression: str):
        self.assertTrue(parse(tokenize(expression)), expression)

    def assertInvalid(self, expression: str):
        self.assertFalse(parse(tokenize(expression)), expression)

    def test_constants_and_propositions(self):
        for expression in ("true", "false", "1", "1abc"):
            self.assertValid(expression)

    def test_unary_formula(self):
        self.assertValid(r"(\neg false)")

    def test_binary_formula(self):
        self.assertValid(r"(\wedge true false)")
        self.assertValid(r"(\rightarrow 1abc (\vee true false))")

    def test_invalid_expressions(self):
        self.assertInvalid(r"(\neg)")
        self.assertInvalid(r"(\wedge true)")
        self.assertInvalid(r"true false")
        self.assertInvalid("@")
        self.assertInvalid(r"(\xor true false)")


if __name__ == "__main__":
    unittest.main()
