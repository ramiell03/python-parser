class EvaluatorError(Exception):
    pass


class Evaluator:
    @staticmethod
    def evaluate(node):

        if hasattr(node, "value"):
            return node.value

        if hasattr(node, "left") and hasattr(node, "right"):
            left = Evaluator.evaluate(node.left)
            right = Evaluator.evaluate(node.right)

            op = node.operator.type

            if op == "PLUS":
                return left + right
            if op == "MINUS":
                return left - right
            if op == "MULTIPLY":
                return left * right
            if op == "DIVIDE":
                if right == 0:
                    raise EvaluatorError("Division by zero")
                return left / right

        raise EvaluatorError("Invalid AST node")