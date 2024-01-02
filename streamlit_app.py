import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded file)
  st.supheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive statistics')
  st.write(dt.describe())
else:
  st.info('Upload a CSV file')
