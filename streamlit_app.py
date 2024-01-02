import streamlit as st 

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green'))

st.write('Your facorite color is ', option)
