import streamlit as st

st.title('st.form')

# Example using 'with' notation

st.header('1.Example of using `with` notation')
st.subheader('Cofee machine')

with st.form('my_form'):
  st.subheader('**Order your coffee**')

 # Input widgets
  coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
  coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
  brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
  serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
  milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
  owncup_val = st.checkbox('Bring own cup')

submitted = st.form_submit_button('Submit')

if submitted:
  st.markdown(f'''
    You have ordered:
    - Coffee bean: `{coffee_bean_val}`
    - Coffee roast: `{coffee_roast_val}`
    - Brewing: `{brewing_val}`
    - Serving type: `{serving_type_val}`
    - Milk: `{milk_val}`
    - Bring own cup: `{owncup_val}`
    ''')
else:
  st.write('Place your order!')
