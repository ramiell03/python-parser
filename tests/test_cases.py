import unittest
from src.evaluator.evaluator import evaluate, EvaluationError


class NumberNode:
    def __init__(self, value):
        self.value = value


class BinaryOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Token:
    def __init__(self, type):
        self.type = type


class TestEvaluator(unittest.TestCase):

    def test_addition(self):
        tree = BinaryOpNode(NumberNode(2), Token("PLUS"), NumberNode(3))
        self.assertEqual(evaluate(tree), 5)

    def test_multiplication(self):
        tree = BinaryOpNode(NumberNode(4), Token("MULTIPLY"), NumberNode(5))
        self.assertEqual(evaluate(tree), 20)

    def test_division_by_zero(self):
        tree = BinaryOpNode(NumberNode(4), Token("DIVIDE"), NumberNode(0))
        with self.assertRaises(EvaluationError):
            evaluate(tree)


if __name__ == "__main__":
    unittest.main()