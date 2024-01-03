import streamlit as st
import pandas as pd

st.title("MSAP 2024 - Factory Data Collection")

st.header("Company Info")
CompanyName = st.text_input('Company Name', '[pre-populate]')
DataEnteredBy = st.text_input('Enter your name', "")
Signature = st.text_input('Sign Here', "")

st.header("Current Factories")
st.subheader("These are the factories we have from last year")
st.write("- To remove a factory from this year's assessment, click the checkbox next to the name and select the delete icon")
st.write("- To add a new factory, click the '+' icon in the last row and enter the factory name")
st.write("- When you are done, click **Submit**")
current_factories = pd.DataFrame({
    'Factory Name':['Factory 1', 'Factory 2', 'Factory 3']
})

st.data_editor(current_factories,
    hide_index=True,
    num_rows="dynamic"
    )
