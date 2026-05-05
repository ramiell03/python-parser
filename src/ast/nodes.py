from graphviz import Digraph
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
        
def pretty_print(node, indent="", last=True):
    """Returns a visual tree representation of the AST"""
    
    if isinstance(node, NumberNode):
        return indent + ("└── " if last else "├── ") + str(node.value) + "\n"

    if isinstance(node, BinaryOpNode):
        result = indent + ("└── " if last else "├── ") + node.operator.type + "\n"
        
        indent += "    " if last else "│   "
        
        result += pretty_print(node.left, indent, False)
        result += pretty_print(node.right, indent, True)
        
        return result

    return indent + "UnknownNode\n"

def visualize_ast(node):
    dot = Digraph()

    def add(n):
        node_id = str(id(n))

        if isinstance(n, NumberNode):
            dot.node(node_id, str(n.value))
            return

        if isinstance(n, BinaryOpNode):
            label = n.operator.type if hasattr(n.operator, "type") else str(n.operator)
            dot.node(node_id, label)

            add(n.left)
            add(n.right)

            dot.edge(node_id, str(id(n.left)))
            dot.edge(node_id, str(id(n.right)))
            return

        dot.node(node_id, str(n))

    add(node)
    return dot