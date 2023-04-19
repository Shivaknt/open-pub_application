import streamlit as st
import pandas as pd
import os
from PIL import Image

st.title('''Welcome  to welcome page 😊😊😊😊
          My new project-OPENPUB WEBAPP using Streamlit Webapp''')
st.image('png.png')


# Experimental Feature

uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "data_dictionary.xlsx"


st.header('Project Information 🥂🍻🥂')

df = pd.read_csv("open_pubs_updated.csv")

st.text('''Let’s assume you are on a Vacation in the United Kingdom with your friends. Just for 
some fun, you decided to go to the Pubs nearby for some drinks. Google Map 
is down because of some issues. 
While searching the internet, you came across https://www.getthedata.com/open-pubs. 
On this website, you found all the pub locations (Specifically Latitude 
and Longitude info). 
In order to impress your friends, you decided to create a Web Application 
with the data available in your hand. 
''')

st.image('images.jpg')

st.header('DATA INFORMATION')

btn_click = st.button("Click Me 👈")

if btn_click == True:
    st.subheader("Here is the data")
    st.balloons()
    st.dataframe(df)
#image = Image.open('images.PNG')

st.header('''Problem statement table for explanation of dataset''')

ds = pd.read_excel("data_dictionary.xlsx")
st.dataframe(ds)


st.header("DATA DESCRIPTION:")
x = df.describe()
x
