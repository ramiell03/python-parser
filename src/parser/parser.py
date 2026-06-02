from src.ast.nodes import NumberNode, BinaryOpNode
from src.tokenizer.tokenizer import Token, EOF

class ParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else Token(EOF)

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token(EOF)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.advance()
        else:
            raise ParserError(
                f"Expected {token_type}, got {self.current_token.type}"
            )

    def factor(self):
        token = self.current_token

        if token.type == "NUMBER":
            self.eat("NUMBER")
            return NumberNode(token.value)

        if token.type == "LPAREN":
            self.eat("LPAREN")
            node = self.expression()
            self.eat("RPAREN")
            return node

        raise ParserError(f"Unexpected token: {token.type}")

    def term(self):
        node = self.factor()

        while self.current_token.type in ("MULTIPLY", "DIVIDE"):
            token = self.current_token
            self.eat(token.type)
            node = BinaryOpNode(node, token, self.factor())

        return node

    def expression(self):
        node = self.term()

        while self.current_token.type in ("PLUS", "MINUS"):
            token = self.current_token
            self.eat(token.type)
            node = BinaryOpNode(node, token, self.term())

        return node

    def parse(self):
        node = self.expression()

        if self.current_token.type != EOF:
            raise ParserError("Unexpected trailing characters")

        return node