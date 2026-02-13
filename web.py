import streamlit as st
from app.agents import DocstringAgent

st.set_page_config(page_title="Docstring Generator", layout="wide")

st.title("🐍 AI Docstring Generator")
st.write("Upload a Python file to auto-generate docstrings.")

uploaded_file = st.file_uploader("Upload .py file", type=["py"])

if uploaded_file:
    code = uploaded_file.read().decode("utf-8")

    st.subheader("Original Code")
    st.code(code, language="python")

    if st.button("Generate Docstrings"):
        agent = DocstringAgent()
        new_code = agent.process_code(code)

        st.subheader("Enhanced Code")
        st.code(new_code, language="python")

        st.download_button(
            "Download Updated File",
            new_code,
            file_name="updated.py"
        )
