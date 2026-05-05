class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberNode({self.value!r})"

    def __eq__(self, other):
        if not isinstance(other, NumberNode):
            return False
        return self.value == other.value


class BinaryOpNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOpNode({self.left!r}, {self.operator!r}, {self.right!r})"

    def __eq__(self, other):
        if not isinstance(other, BinaryOpNode):
            return False
        return (
            self.left == other.left and
            self.operator == other.operator and
            self.right == other.right
        )