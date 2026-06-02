from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import base64
import uuid

from src.ast.nodes import pretty_print, visualize_ast
from src.tokenizer.tokenizer import Tokenizer
from src.parser.parser import Parser, ParserError
from src.evaluator.evaluator import Evaluator, EvaluatorError


# ----------------------------
# APP INIT
# ----------------------------
app = FastAPI(
    title="Math Expression Parser API",
    description="Mini compiler API (Tokenizer → Parser → AST → Evaluator)",
    version="1.0.0",
)


# ----------------------------
# STATIC FILES (FOR DOWNLOAD)
# ----------------------------
STATIC_DIR = Path(__file__).parent / "static"
STATIC_DIR.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


# ----------------------------
# REQUEST / RESPONSE MODELS
# ----------------------------
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
    image_base64: str
    image_url: str


# ----------------------------
# CORE PIPELINE
# ----------------------------
def process_expression(expression: str):
    tokenizer = Tokenizer(expression)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    result = Evaluator.evaluate(ast)

    return tokens, ast, result


# ----------------------------
# EVALUATE ENDPOINT
# ----------------------------
@app.post("/evaluate", response_model=EvaluateResponse)
async def evaluate(request: ExpressionRequest):
    try:
        _, _, result = process_expression(request.expression)

        return {
            "expression": request.expression,
            "result": result
        }

    except ParserError as e:
        raise HTTPException(status_code=400, detail=f"Syntax Error: {str(e)}")

    except EvaluatorError as e:
        raise HTTPException(status_code=400, detail=f"Evaluation Error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ----------------------------
# TOKENS ENDPOINT
# ----------------------------
@app.post("/tokens", response_model=TokensResponse)
async def get_tokens(request: ExpressionRequest):
    try:
        tokenizer = Tokenizer(request.expression)
        tokens = tokenizer.tokenize()

        token_list = [
            {"type": t.type, "value": t.value}
            for t in tokens
            if t.type != "EOF"
        ]

        return {
            "expression": request.expression,
            "tokens": token_list
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ----------------------------
# AST ENDPOINT (FIXED + DOWNLOAD SUPPORT)
# ----------------------------
@app.post("/ast", response_model=ASTResponse)
async def get_ast(request: ExpressionRequest):
    try:
        tokenizer = Tokenizer(request.expression)
        tokens = tokenizer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        # text AST
        tree_visual = pretty_print(ast)

        # graph image
        graph = visualize_ast(ast)
        img_bytes = graph.pipe(format="png")

        # save file
        file_id = str(uuid.uuid4())
        file_path = STATIC_DIR / f"{file_id}.png"

        with open(file_path, "wb") as f:
            f.write(img_bytes)

        return {
            "expression": request.expression,
            "ast": tree_visual,
            "image_base64": base64.b64encode(img_bytes).decode("utf-8"),
            "image_url": f"/static/{file_id}.png"
        }

    except ParserError as e:
        raise HTTPException(status_code=400, detail=f"Syntax Error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ----------------------------
# ROOT
# ----------------------------
@app.get("/")
async def root():
    return {
        "message": "Math Expression Parser API",
        "endpoints": {
            "evaluate": "POST /evaluate",
            "tokens": "POST /tokens",
            "ast": "POST /ast"
        }
    }