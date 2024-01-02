import streamlit as st

st.title("MSAP 2024 - Factory Data Collection")

DataEnteredBy = st.text_input
Signature = st.text_input

st.header("Company Info")
st.write("Company Name:", '[pre-populate]')
st.write("Data entered by:", DataEnteredBy)
st.write("Signature:", Signature)
