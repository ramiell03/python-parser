import streamlit as st
import requests

st.set_page_config(
    page_title="Math Expression Parser",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Math Expression Parser")
st.markdown("Enter a mathematical expression to parse, tokenize, and evaluate.")

API_URL = "http://localhost:8000"

expression = st.text_input(
    "Expression",
    value="3 + 4 * 2",
    placeholder="e.g., (10 - 2) / 4 + 3 * 5"
)

col1, col2, col3 = st.columns(3)

with col1:
    evaluate_btn = st.button("🔢 Evaluate", use_container_width=True)
with col2:
    tokens_btn = st.button("🔤 Tokens", use_container_width=True)
with col3:
    ast_btn = st.button("🌳 AST", use_container_width=True)

st.divider()

if evaluate_btn:
    with st.spinner("Evaluating..."):
        try:
            response = requests.post(
                f"{API_URL}/evaluate",
                json={"expression": expression}
            )
            if response.status_code == 200:
                data = response.json()
                st.success(f"Result: **{data['result']}**")
            else:
                st.error(f"Error: {response.json()['detail']}")
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to API. Make sure the server is running on port 8000.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if tokens_btn:
    with st.spinner("Tokenizing..."):
        try:
            response = requests.post(
                f"{API_URL}/tokens",
                json={"expression": expression}
            )
            if response.status_code == 200:
                data = response.json()
                st.subheader("Tokens")
                for token in data['tokens']:
                    if token['type'] != 'EOF':
                        st.code(f"{token['type']}: {token['value']}")
            else:
                st.error(f"Error: {response.json()['detail']}")
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to API. Make sure the server is running on port 8000.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if ast_btn:
    with st.spinner("Building AST..."):
        try:
            response = requests.post(
                f"{API_URL}/ast",
                json={"expression": expression}
            )
            if response.status_code == 200:
                data = response.json()
                st.subheader("Abstract Syntax Tree")
                st.code(data['ast'], language="python")
            else:
                st.error(f"Error: {response.json()['detail']}")
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to API. Make sure the server is running on port 8000.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()
st.markdown("""
**Supported Operations:**
- Addition (`+`), Subtraction (`-`)
- Multiplication (`*`), Division (`/`)
- Parentheses (`(` and `)`)
- Integers and floating-point numbers

**Examples:**
- `3 + 4 * 2` → 11
- `(3 + 4) * 2` → 14
- `10 / 2 - 3` → 2.0
""")