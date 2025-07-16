# html_interpreter.py
import streamlit as st

st.set_page_config(page_title="HTML Interpreter", layout="centered")
st.title(" HTML Live Interpreter")

html_code = st.text_area("✍ Write HTML code below", height=300, placeholder="<h1>Hello World!</h1>")
st.markdown("### Live Preview")

if html_code:
    st.components.v1.html(html_code, height=400, scrolling=True)
else:
    st.info("🖋 Your live output will appear here as you type.")
