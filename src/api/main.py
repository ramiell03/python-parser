from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
import sys
import os
from pathlib import Path
from fastapi.staticfiles import StaticFiles

# Define a fixed absolute path for static files
STATIC_DIR = Path(__file__).parent / "static"
STATIC_DIR.mkdir(exist_ok=True)


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ast.nodes import pretty_print, visualize_ast
from src.tokenizer.tokenizer import Tokenizer
from src.parser.parser import Parser, ParserError
from src.evaluator.evaluator import Evaluator, EvaluatorError


app = FastAPI(
    title="Math Expression Parser API",
    description="""
    A mini-compiler API for mathematical expressions.

    Features:
    - Tokenization
    - Parsing (AST generation)
    - Evaluation

    Supports:
    +, -, *, / and parentheses
    """,
    version="1.0.0",

)


class ExpressionRequest(BaseModel):
    expression: str

    class Config:
        schema_extra = {
            "example": {
                "expression": "3 + 5 * (2 - 1)"
            }
        }


class EvaluateResponse(BaseModel):
    expression: str
    result: Union[int, float]

    class Config:
        schema_extra = {
            "example": {
                "expression": "3 + 5 * 2",
                "result": 13
            }
        }


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


@app.post(
    "/evaluate",
    response_model=EvaluateResponse,
    summary="Evaluate expression",
    tags=["Evaluation"],
    description="Parses and evaluates a mathematical expression."
)
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


@app.post(
    "/tokens",
    response_model=TokensResponse,
    summary="Get tokens",
    tags=["Analysis"],
    description="Tokenizes a mathematical expression."
)
async def get_tokens(request: ExpressionRequest):
    try:
        tokenizer = Tokenizer(request.expression)
        tokens = tokenizer.tokenize()
        token_list = [{"type": t.type, "value": t.value} for t in tokens]
        return {"expression": request.expression, "tokens": token_list}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


import base64
from io import BytesIO

@app.post(
    "/ast",
    response_model=ASTResponse,
    summary="Get AST",
    tags=["Analysis"],
    description="Generates the abstract syntax tree for a mathematical expression."
)
async def get_ast(request: ExpressionRequest):
    try:
        tokenizer = Tokenizer(request.expression)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()

        tree_visual = pretty_print(ast)
        graph = visualize_ast(ast)

        # Render to bytes instead of file
        img_bytes = graph.pipe(format="png")
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

        return {
            "expression": request.expression,
            "ast": tree_visual,
            "image_base64": img_base64
        }

    except ParserError as e:
        raise HTTPException(status_code=400, detail=f"Syntax Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")
# Mount using the same absolute path
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

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