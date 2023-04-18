import streamlit as st
import pandas as pd 
import numpy as np


df = pd.read_csv("open_pubs_updated.csv")

# make header
st.header("Location of all Bars in UK based on the Local Authority: 🍷🥂🍻🥂🍷🍷")
# enter either postal code or local authority

local_auth = st.selectbox('Select the area in which you want to search', set(df['local_authority']))
button_1 = st.button("Search")

if button_1:
    df_new = df.loc[(df['local_authority'] == local_auth)]
    st.text("The Pubs in this Region are:")
    st.dataframe(df_new)
    st.map(df_new)
