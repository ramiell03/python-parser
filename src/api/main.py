from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.tokenizer.tokenizer import Tokenizer
from src.parser.parser import Parser, ParserError
from src.evaluator.evaluator import Evaluator, EvaluatorError

app = FastAPI(
    title="Math Expression Parser API",
    description="API for parsing and evaluating mathematical expressions",
    version="1.0.0"
)


class ExpressionRequest(BaseModel):
    expression: str


class EvaluateResponse(BaseModel):
    expression: str
    result: Union[int, float]


class TokensResponse(BaseModel):
    expression: str
    tokens: list


class ASTResponse(BaseModel):
    expression: str
    ast: str


def process_expression(expression: str):
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    result = Evaluator.evaluate(ast)
    return tokens, ast, result


@app.post("/evaluate", response_model=EvaluateResponse)
async def evaluate(request: ExpressionRequest):
    try:
        _, _, result = process_expression(request.expression)
        return {"expression": request.expression, "result": result}
    except ParserError as e:
        raise HTTPException(status_code=400, detail=f"Syntax Error: {str(e)}")
    except EvaluatorError as e:
        raise HTTPException(status_code=400, detail=f"Evaluation Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")


@app.post("/tokens", response_model=TokensResponse)
async def get_tokens(request: ExpressionRequest):
    try:
        tokenizer = Tokenizer(request.expression)
        tokens = tokenizer.tokenize()
        token_list = [{"type": t.type, "value": t.value} for t in tokens]
        return {"expression": request.expression, "tokens": token_list}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/ast", response_model=ASTResponse)
async def get_ast(request: ExpressionRequest):
    try:
        tokenizer = Tokenizer(request.expression)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        return {"expression": request.expression, "ast": repr(ast)}
    except ParserError as e:
        raise HTTPException(status_code=400, detail=f"Syntax Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {
        "message": "Math Expression Parser API",
        "endpoints": {
            "evaluate": "POST /evaluate - Evaluate expression",
            "tokens": "POST /tokens - Get token list",
            "ast": "POST /ast - Get AST representation"
        }
    }