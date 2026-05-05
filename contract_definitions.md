# Token types (constants)
NUMBER = "NUMBER"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
LPAREN = "LPAREN"
RPAREN = "RPAREN"
EOF = "EOF"


🔹 2. Define Token Structure
class Token:
    def __init__(self, type: str, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

👉 This MUST be used by everyone.


🔹 3. Final Grammar (Write in docs)
Expression → Term ((+ | -) Term)*
Term       → Factor ((* | /) Factor)*
Factor     → NUMBER | '(' Expression ')'


🔹 4. Define AST Contract (IMPORTANT)

Even if Member 3 implements it, YOU define it:

class NumberNode:
    value

class BinaryOpNode:
    left
    operator
    right


🔹 5. Define Interface Contracts

Create docs/interfaces.md:

def tokenize(input: str) -> list:
    pass

def parse(tokens: list) -> object:
    pass

def evaluate(ast) -> float:
    pass