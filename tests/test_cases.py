import ast
import unittest

from src.tokenizer.tokenizer import Tokenizer
from src.parser.parser import Parser
from src.evaluator.evaluator import Evaluator
from src.ast.nodes import pretty_print, visualize_ast, visualize_ast


class TestMathParser(unittest.TestCase):

    # 🔹 1. TOKENIZER TEST
    def test_tokenizer(self):
        expr = "3 + 5"
        tokens = Tokenizer(expr).tokenize()

        self.assertEqual(tokens[0].type, "NUMBER")
        self.assertEqual(tokens[1].type, "PLUS")
        self.assertEqual(tokens[2].type, "NUMBER")

    # 🔹 2. PARSER TEST (AST STRUCTURE)
    def test_parser(self):
        expr = "3 + 5 * 2"
        tokens = Tokenizer(expr).tokenize()
        ast = Parser(tokens).parse()

        # Root should be PLUS
        self.assertEqual(ast.operator.type, "PLUS")

        # Right side should be MULTIPLY
        self.assertEqual(ast.right.operator.type, "MULTIPLY")

    # 🔹 3. EVALUATOR TEST
    def test_evaluator(self):
        expr = "3 + 5 * 2"
        tokens = Tokenizer(expr).tokenize()
        ast = Parser(tokens).parse()
        result = Evaluator.evaluate(ast)

        self.assertEqual(result, 13)

    # 🔥 4. AST VISUALIZATION TEST (NEW)
    def test_ast_visualization(self):
        expr = "3 + 5 * 2"
        tokens = Tokenizer(expr).tokenize()
        ast = Parser(tokens).parse()

        tree = pretty_print(ast)

        expected = (
            "└── PLUS\n"
            "    ├── 3\n"
            "    └── MULTIPLY\n"
            "        ├── 5\n"
            "        └── 2\n"
        )

        self.assertEqual(tree, expected)

    # 🔹 5. ERROR TEST (INVALID INPUT)
    def test_invalid_expression(self):
        expr = "3 + * 5"

        with self.assertRaises(Exception):
            tokens = Tokenizer(expr).tokenize()
            Parser(tokens).parse()

    # 🔹 6. DIVISION BY ZERO
    def test_division_by_zero(self):
        expr = "10 / 0"
        tokens = Tokenizer(expr).tokenize()
        ast = Parser(tokens).parse()

        with self.assertRaises(Exception):
            Evaluator.evaluate(ast)

dot = visualize_ast(ast)
dot.render("ast_tree", format="png", view=True)

if __name__ == "__main__":
    unittest.main()