✅ What to do
⚙️ Commands to run
📚 Libraries/tools
⚠️ Challenges & pitfalls
🎯 What success looks like

No fluff — just what you need to build this properly.

🔷 STEP 1: PROJECT SETUP
✅ What to do
Create GitHub repo
Initialize project locally
Create folder structure
⚙️ Commands
git clone https://github.com/your-repo/math-expression-parser.git
cd math-expression-parser

mkdir src tests docs
cd src
mkdir tokenizer parser ast evaluator api ui
touch main.py
📚 Libraries
None yet (pure Python)
⚠️ Challenges
Bad structure early → chaos later
No Git discipline → overwritten code
🎯 Success
Everyone can clone and run project
Clean folders exist
🔷 STEP 2: TOKENIZER (LEXICAL ANALYZER)
✅ What to do
Read input string character by character
Group characters into tokens
⚙️ Key logic
Loop through string
Detect:
digits → build numbers
symbols → operators
spaces → ignore
📚 Libraries
Optional: re (regex)
import re
⚙️ Example Commands

Run test:

python src/tokenizer/tokenizer.py
⚠️ Challenges
Handling floats (12.34)

Avoiding:

"12..3" ❌

Unknown characters:

"3 + a" ❌
🎯 Success

Input:

"12 + 3.5"

Output:

[NUMBER(12), PLUS, NUMBER(3.5)]
🔷 STEP 3: PARSER (SYNTAX ANALYZER)
✅ What to do
Convert tokens → AST using grammar
⚙️ Functions to implement
parse_expression()
parse_term()
parse_factor()
⚙️ Commands
python src/parser/parser.py
📚 Libraries
None (pure logic)
⚠️ Challenges
Recursion errors
Infinite loops
Incorrect precedence
🎯 Success

Input:

3 + 5 * 2

AST:

+
├── 3
└── *
    ├── 5
    └── 2
🔷 STEP 4: AST IMPLEMENTATION
✅ What to do
Create node classes
📚 Libraries
Optional:
from dataclasses import dataclass
⚠️ Challenges
Keeping structure simple
Debugging tree
🎯 Success

You can print AST clearly.

🔷 STEP 5: EVALUATOR
✅ What to do
Traverse AST recursively
Compute result
⚙️ Commands
python src/evaluator/evaluator.py
⚠️ Challenges
Division by zero
Wrong recursion logic
🎯 Success
(3 + 2) * 4 → 20
🔷 STEP 6: ERROR HANDLING
✅ What to do
Create custom exceptions
⚙️ Example
class LexerError(Exception): pass
class ParserError(Exception): pass
class EvaluationError(Exception): pass
⚠️ Challenges
Forgetting to raise errors
Poor error messages
🎯 Success
3 + * 5 → Syntax Error
🔷 STEP 7: INTEGRATION (CORE ENGINE)
✅ What to do

Combine everything:

def process_expression(expr):
    tokens = tokenize(expr)
    ast = parse(tokens)
    result = evaluate(ast)
    return result
⚙️ Commands
python src/main.py
⚠️ Challenges
Modules not matching contracts
Import errors
🎯 Success

Single function runs full pipeline.

🔷 STEP 8: API (FastAPI)
✅ What to do

Expose your compiler as a web service

⚙️ Install
pip install fastapi uvicorn
⚙️ Run server
uvicorn src.api.main:app --reload
📚 Libraries
FastAPI
Uvicorn
⚠️ Challenges
Importing your core modules correctly
Handling errors in API responses
🎯 Success

You can call:

POST /evaluate
🔷 STEP 9: SWAGGER DOCUMENTATION
✅ What to do
Use FastAPI built-in docs
🌐 Access:
http://127.0.0.1:8000/docs
⚠️ Challenges
Poor endpoint descriptions
No examples
🎯 Success

Interactive UI where user can test API.

🔷 STEP 10: UI (FRONTEND)
OPTION A: Streamlit (Recommended)
⚙️ Install
pip install streamlit
⚙️ Run
streamlit run src/ui/app.py
📚 Library
Streamlit
⚠️ Challenges
Connecting to API
Handling errors visually
🎯 Success

User types expression → sees result instantly

🔷 STEP 11: TESTING
✅ What to do
Write test cases
⚙️ Run tests
python -m unittest
📚 Libraries
unittest (built-in)
Optional: pytest
⚠️ Challenges
Not testing edge cases
Ignoring invalid inputs
🎯 Success

All tests pass automatically.

🔷 STEP 12: DOCUMENTATION (FINAL REPORT)
✅ Include:
Architecture diagram
Grammar explanation
API screenshots (Swagger)
UI screenshots
⚠️ Challenges
Weak explanations
No diagrams
🎯 Success

Clear, professional report

FINAL BALANCED TEAM STRUCTURE (PAIRING MODEL)

We split into 3 pairs (2 people each):

Each pair owns a complete subsystem
One “lead” + one “support”
Ensures fairness + collaboration + backup


🧩 🔷 PAIR 1 — ARCHITECTURE + TOKENIZER (FOUNDATION LAYER)
👥 Members:
Member 1 (Lead)
Member 2 (Support)
🔷 Responsibilities

🧠 Member 1 (Lead – System Architect)
Project setup (Git, folders)
Define token specifications
Define grammar rules formally
Ensure system consistency

🛠️ Member 2 (Support – Tokenizer Developer)
Implement tokenizer logic
Handle numbers, operators, validation
Test token output
🔗 Why this pairing works

Tokenizer depends on:

token rules (Member 1 defines)
implementation (Member 2 builds)

👉 Perfect dependency chain

🎯 Success
Clean input → token pipeline working
No ambiguity in token rules


🧩 🔷 PAIR 2 — PARSER + AST (CORE COMPILER ENGINE 🔥)
👥 Members:
Member 3 (Lead)
Member 4 (Support)
🔷 Responsibilities

🧠 Member 3 (Lead – Parser Architect)
Implements recursive descent parser
Enforces grammar rules
Controls precedence logic

🛠️ Member 4 (Support – AST Engineer)
Builds AST node system
Ensures parser correctly builds tree
Debug & visualize AST
🔗 Why this pairing is CRITICAL

This is the heart of your project:

parser creates structure
AST represents meaning

👉 Most complex part → needs 2 people

🎯 Success
Expression → correct AST tree
Proper operator precedence respected

🧩 🔷 PAIR 3 — EVALUATION + PRODUCT LAYER (ENGINE + APPLICATION)
👥 Members:
Member 5 (Lead)
Member 6 (Support)

🔷 Responsibilities
🧠 Member 5 (Lead – Evaluation + Testing Engineer)
Implements AST evaluator
Handles recursion logic
Builds error handling system
Writes tests (unit + edge cases)


🛠️ Member 6 (Support – API + UI Developer)
Builds FastAPI backend
Creates endpoints:
/evaluate
/tokens
/ast
Builds Streamlit UI
Handles Swagger documentation
Final integration + demo
🔗 Why this pairing works
Evaluator is backend logic
API/UI is product layer

👉 Member 6 consumes Member 5 output

🎯 Success
Working API + UI
Expression fully evaluated from browser
Swagger documentation visible
Tested system