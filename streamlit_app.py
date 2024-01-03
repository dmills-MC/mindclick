import streamlit as st
import pandas as pd

st.title("MSAP 2024 - Factory Data Collection")

st.header("Company Info")
CompanyName = st.text_input('Company Name', '[pre-populate]')
DataEnteredBy = st.text_input('Enter your name', "")
Signature = st.text_input('Sign Here', "")

st.header("Factory Overview")
st.subheader("These are the factories we have from last year")
lst = ['Factory 1', 'Factory 2', 'Factory 3']
for i in lst:
    st.markdown("- " + i)

st.header("Current Factories")
pd.DataFrame({
    'Factory Name':['Factory 1', 'Factory 2', 'Factory 3']
    num_rows="dynamic"
})



remove_factories = st.radio("Do you need to remove any of these factories for this year?", ['Yes', 'No'])
if remove_factories == 'Yes':
    st.text_input('Factory Name')
else:
    st.write()

add_factories = st.radio("Do you need to add any new factories for this year?", ['Yes', 'No'])
