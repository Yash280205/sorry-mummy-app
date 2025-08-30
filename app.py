import streamlit as st
import streamlit.components.v1 as components

# Load HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Set page config
st.set_page_config(page_title="Sorry Mummy ❤️", layout="centered")

st.title("💌 A Special Message for Mom")
st.write("This is a small interactive message app made with love.")

# Render HTML
components.html(html_code, height=800, scrolling=True)
