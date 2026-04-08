import streamlit as st
import pandas as pd

st.title('Streamlit Project')

st.write("News Classification")

#Taking input value from user
data = st.text_area("Enter News for Classification")
if st.button('Submit'):
    d = {'news':[data]}
    df = pd.DataFrame(d)
    st.write(df)
