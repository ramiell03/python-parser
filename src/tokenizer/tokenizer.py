#import token definitions

from dataclasses import dataclass

class LexerError(Exception):
    pass

#import token definition
@dataclass
class Token:
    type: str
    value: any = None

#token types
NUMBER = "NUMBER"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
LPAREN = "LPAREN"
RPAREN = "RPAREN"
EOF = "EOF"

#token definition
def tokenize(text: str):
    tokens = []
    i = 0

    while i < len(text):
        char = text[i]

        if char.isspace():
            i += 1
            continue

        # Number parsing
        if char.isdigit() or char == '.':
            num_str = char
            i += 1

            while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                num_str += text[i]
                i += 1

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
            raise LexerError(f"Invalid character '{char}' at position {i}")

        i += 1

    tokens.append(Token(EOF))
    return tokens

#test block
if __name__ == "__main__":
    expr = "12 + 3.5 * (2 - 1)"
    print(tokenize(expr))