# 🧮 Mathematical Expression Parser (Mini-Compiler)

## 📌 Project Overview
This project implements a **Python-based parser for well-formed mathematical expressions**, inspired by compiler design principles.

The system takes a mathematical expression as input, validates its syntax, builds an internal representation (Abstract Syntax Tree), and evaluates the result.

---

## 🎯 Objectives
- Design a mini-compiler for arithmetic expressions
- Apply concepts of:
  - Lexical Analysis (Tokenization)
  - Syntax Analysis (Parsing)
  - Abstract Syntax Tree (AST)
  - Expression Evaluation
- Ensure proper handling of operator precedence and parentheses

---

## ⚙️ Features
- Supports arithmetic operators:
  - `+` Addition
  - `-` Subtraction
  - `*` Multiplication
  - `/` Division
- Supports parentheses `( )`
- Handles integer and floating-point numbers
- Detects invalid expressions
- Evaluates valid expressions

---

## 🧠 Grammar Definition


Expression → Term ((+ | -) Term)*
Term → Factor ((* | /) Factor)*
Factor → NUMBER | '(' Expression ')'

3. Project Folder Structure (IMPORTANT)

Here’s a clean and scalable structure:

math-expression-parser/
│
├── src/                    # Main source code
│   ├── tokenizer/         # Lexical analysis
│   │   └── tokenizer.py
│   │
│   ├── parser/            # Syntax analysis
│   │   └── parser.py
│   │
│   ├── ast/               # AST structure
│   │   └── nodes.py
│   │
│   ├── evaluator/         # Execution / evaluation
│   │   └── evaluator.py
│   │
│   └── main.py            # Entry point
│
├── tests/                 # Test cases
│   └── test_cases.py
│
├── docs/                  # Documentation
│   └── project_report.md
│
├── requirements.txt       # Dependencies (if any)
├── README.md
└── .gitignore

🔷 4. What Each Folder Does
📁 tokenizer/
Converts input string → tokens
📁 parser/
Uses grammar rules
Builds AST
📁 ast/
Defines tree structure:
NumberNode
BinaryOpNode
📁 evaluator/
Walks the tree
Produces result
📁 main.py
Connects everything
User input → output