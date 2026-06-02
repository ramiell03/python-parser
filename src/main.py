from src.tokenizer.tokenizer import Tokenizer
from src.parser.parser import Parser
from src.evaluator.evaluator import Evaluator


def main():
    print("🧮 Math Expression Parser CLI")
    print("Type 'exit' to quit\n")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == "exit":
            break

        try:
            # -------------------------
            # TOKENIZE
            # -------------------------
            tokenizer = Tokenizer(expression)
            tokens = tokenizer.tokenize()

            print("\nTokens:")
            for t in tokens:
                if t.type != "EOF":
                    print(f"  {t.type}: {t.value}")

            # -------------------------
            # PARSE
            # -------------------------
            parser = Parser(tokens)
            ast = parser.parse()

            print("\nAST:")
            print(ast)

            # -------------------------
            # EVALUATE
            # -------------------------
            result = Evaluator.evaluate(ast)

            print("\nResult:", result)
            print("-" * 40)

        except Exception as e:
            print("Error:", str(e))
            print("-" * 40)


if __name__ == "__main__":
    main()