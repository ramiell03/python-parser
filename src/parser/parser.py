from src.ast.nodes import NumberNode, BinaryOpNode
from src.tokenizer.tokenizer import Token

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if tokens else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token('EOF', None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.advance()
        else:
            raise ParserError(f"Invalid syntax. Expected {token_type}, got {self.current_token.type}")

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return NumberNode(token.value)
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node
        raise ParserError(f"Invalid token: {token.type}")

    def term(self):
        node = self.factor()
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
            node = BinaryOpNode(left=node, operator=token, right=self.factor())
        return node

    def expression(self):
        node = self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')
            node = BinaryOpNode(left=node, operator=token, right=self.term())
        return node

    def parse(self):
        root = self.expression()
        if self.current_token.type != 'EOF':
            raise ParserError("Unexpected characters at end of expression")
        return root