import streamlit as st
import requests
import base64
import os

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="Math Expression Parser",
    layout="centered"
)

st.title("🧮 Math Expression Parser")
st.markdown("Enter a mathematical expression to analyze.")

API_URL = os.getenv("API_URL", "http://localhost:8000")


# ----------------------------
# INPUT
# ----------------------------
expression = st.text_input(
    "Expression",
    value="3 + 4 * 2",
    placeholder="e.g. (10 - 2) / 4 + 3 * 5"
)

col1, col2, col3 = st.columns(3)

evaluate_btn = col1.button("Evaluate")

tokens_btn = col2.button("Tokens")

ast_btn = col3.button("AST")

st.divider()


# ----------------------------
# EVALUATE
# ----------------------------
if evaluate_btn:
    try:
        response = requests.post(
            f"{API_URL}/evaluate",
            json={"expression": expression}
        )

        data = response.json()

        if response.status_code == 200:
            st.success(f"Result: {data['result']}")
        else:
            st.error(data.get("detail", "Error"))

    except Exception as e:
        st.error(str(e))


# ----------------------------
# TOKENS
# ----------------------------
if tokens_btn:
    try:
        response = requests.post(
            f"{API_URL}/tokens",
            json={"expression": expression}
        )

        data = response.json()

        if response.status_code == 200:
            st.subheader("Tokens")

            for t in data["tokens"]:
                st.code(f"{t['type']} : {t['value']}")

        else:
            st.error(data.get("detail", "Error"))

    except Exception as e:
        st.error(str(e))


# ----------------------------
# AST
# ----------------------------
if ast_btn:
    try:
        response = requests.post(
            f"{API_URL}/ast",
            json={"expression": expression}
        )

        data = response.json()

        if response.status_code == 200:
            st.subheader("AST (Text)")
            st.code(data["ast"], language="text")

            st.subheader("AST (Graph)")

            # ----------------------------
            # IMAGE DISPLAY (NO PIL)
            # ----------------------------
            img_bytes = base64.b64decode(data["image_base64"])
            st.image(img_bytes, use_container_width=True)

            # ----------------------------
            # DOWNLOAD BUTTON
            # ----------------------------
            st.download_button(
                label="⬇️ Download AST Image",
                data=requests.get(API_URL + data["image_url"]).content,
                file_name="ast.png",
                mime="image/png"
            )

        else:
            st.error(data.get("detail", "Error"))

    except Exception as e:
        st.error(str(e))


# ----------------------------
# FOOTER
# ----------------------------
st.divider()

st.markdown("""
### Supported operations
- Addition (+), Subtraction (-)
- Multiplication (*), Division (/)
- Parentheses ( )

### Example
- `3 + 4 * 2`
- `(10 - 2) / 4 + 3 * 5`
""")