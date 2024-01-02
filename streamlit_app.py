import streamlit as st

st.title("MSAP 2024 - Factory Data Collection")

st.header("Company Info")
CompanyName = st.text_input('Company Name', '[pre-populate]')
DataEnteredBy = st.text_input('Enter your name', "")
Signature = st.text_input('Sign Here', "")

st.header("Factory Overview")
lst = ['a', 'b', 'c']

for i in lst:
    st.markdown("- " + I)
