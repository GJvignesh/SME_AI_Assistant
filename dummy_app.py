import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

logo = Image.open('images/gen_ai.png')
st.set_page_config(layout='wide')
st.text('Welcome to SME AI Assistant POC App')
st.image(logo, width=500)
st.divider()
st.header('this is header')
st.subheader('this is sub header')
st.text('this is text area')
st.caption('this is caption')
st.markdown('#this is markdown#')

st.divider()
col1, col2, col3 = st.columns(3)
col1.metric('Temp', '70', '1.2 F')
col2.metric('Wind', '30kmph', '-8%')
col3.metric('Humidity', '86%', '4%')


# Selectors
# Radio button
genre = st.radio(
    "What is your car name?",
    ('one', 'two', 'three')
)

if genre == 'one':
    st.write('Welcome GJ')

# Select box
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile Phone')
)

user_input = st.text_input('label goes here', placeholder='default text goes here')
if st.button('Submit'):
    if user_input:
        st.write(user_input)