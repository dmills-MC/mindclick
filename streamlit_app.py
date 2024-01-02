import streamlit as st

st.title('st.experimental_get_query_params')

st.header('2. contents')
st.write(st.experimental_get_query_params())

st.header(3. retrieve')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname][0]

st.write(f'Hello **{firstname} {surname}**')
