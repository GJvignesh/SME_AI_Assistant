import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from preprocessing_module import preprocessing
from constants import project_list
import utility_functions

logo = Image.open('images/gen_ai.png')
#st.set_page_config(layout='wide')
st.subheader('Welcome to Virtual Subject matter expert POC App')

st.image(logo, width=300)
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric('Margins app development project', '80%', '2%')
col2.metric('React UI for pharma client project', '90%', '-8%')
col3.metric('Mobile app for grocery store project', '40%', '4%')
col4.metric('New project placeholder', '-0%', '-0%')


# Selectors
# Radio button
# genre = st.radio(
#     "Please select your project",
#     ('Margins app development', 'React UI for pharma client', 'Mobile app for grocery store')
# )
#
# if genre == 'Margins app development':
#     st.write('You have selected')


# Select box
option = st.selectbox(
    'Please select the project which you like to know about',
    (project_list[0], project_list[1], project_list[2])
)

print(option)
user_input = st.text_input('Please enter the query about project',
                           placeholder='example: What are all pending development Jira task in our project')


if st.button('Submit'):
    if user_input:
        text = 'Querying info about ' + str(option) + ' Project'
        project_data = utility_functions.get_project_meta_data(option)
        # Initialize custom pre-processor module
        pp = preprocessing.Preprocess()
        processed_project_meta_data = pp.pre_preprocess_text(project_data)
        st.write(processed_project_meta_data)
