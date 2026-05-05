from dataclasses import dataclass

class LexerError(Exception):
    pass

@dataclass
class Token:
    type: str
    value: any = None

NUMBER = "NUMBER"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
LPAREN = "LPAREN"
RPAREN = "RPAREN"
EOF = "EOF"


class Tokenizer:
    def __init__(self, text: str):
        self.text = text
        self.i = 0

    def tokenize(self):
        tokens = []

        while self.i < len(self.text):
            char = self.text[self.i]

            if char.isspace():
                self.i += 1
                continue

            # Numbers
            if char.isdigit() or char == '.':
                num_str = char
                self.i += 1

                while self.i < len(self.text) and (self.text[self.i].isdigit() or self.text[self.i] == '.'):
                    num_str += self.text[self.i]
                    self.i += 1

                if num_str == ".":
                    raise LexerError("Invalid number: '.'")

                if num_str.count('.') > 1:
                    raise LexerError(f"Invalid number format: {num_str}")

                value = float(num_str) if '.' in num_str else int(num_str)
                tokens.append(Token(NUMBER, value))
                continue

            # Operators
            if char == '+':
                tokens.append(Token(PLUS, char))
            elif char == '-':
                tokens.append(Token(MINUS, char))
            elif char == '*':
                tokens.append(Token(MULTIPLY, char))
            elif char == '/':
                tokens.append(Token(DIVIDE, char))
            elif char == '(':
                tokens.append(Token(LPAREN, char))
            elif char == ')':
                tokens.append(Token(RPAREN, char))
            else:
                raise LexerError(f"Invalid character '{char}' at position {self.i}")

            self.i += 1

        tokens.append(Token(EOF))
        return tokens

#test block
if __name__ == "__main__":
    expr = "12 + 3.5 * (2 - 1)"
    tokenizer = Tokenizer(expr)
    print(tokenizer.tokenize())