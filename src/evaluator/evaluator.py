class EvaluationError(Exception):
    pass


def evaluate(node):
    # Case 1: Number
    if hasattr(node, 'value'):
        return node.value

    # Case 2: Binary Operation
    if hasattr(node, 'left') and hasattr(node, 'right'):
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)

        op = node.operator.type

        if op == "PLUS":
            return left_val + right_val

        elif op == "MINUS":
            return left_val - right_val

        elif op == "MULTIPLY":
            return left_val * right_val

        elif op == "DIVIDE":
            if right_val == 0:
                raise EvaluationError("Division by zero")
            return left_val / right_val

    raise EvaluationError("Invalid AST node")


# 🔥 TEST BLOCK
if __name__ == "__main__":
    print("RUNNING TEST...")

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

    # simulate: 3 + 5
    tree = BinaryOpNode(
        NumberNode(3),
        Token("PLUS"),
        BinaryOpNode(
        NumberNode(5),
        Token("MULTIPLY"),
        NumberNode(2),
    )
   ) 
    print(evaluate(tree)),