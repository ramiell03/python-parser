from tokenizer.tokenizer import tokenize
from parser.parser import parse
from evaluator.evaluator import evaluate

expression = input("Enter expression: ")

tokens = tokenize(expression)
ast = parse(tokens)
result = evaluate(ast)

print("Result:", result)