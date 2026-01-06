import streamlit as st

st.title("Simple Dropdown App")

choice = st.selectbox(
    "Pick a letter:",
    ["A", "B", "C", "D"]
)

st.write("You selected:", choice)
