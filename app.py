import time

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

import constants
from preprocessing_module import preprocessing
from constants import project_list
import utility_functions
import LLM.model as model

# c1, c2 = st.columns([2, 2])
# c2.title('Welcome to Virtual Subject Matter Expert App (POC)')
logo = Image.open('images/gen_ai.png')
# c1.image(logo)
st.set_page_config(layout='wide')

st.subheader('Welcome to Virtual Subject Matter Expert App (POC)')
st.image(logo, width=300)
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric('Margins app development project', '80%', '2%')
col2.metric('React UI for pharma client project', '90%', '-8%')
col3.metric('Mobile app for grocery store project', '40%', '4%')
col4.metric('New project placeholder', '-0%', '-0%')


# Select box
option = st.selectbox(
    'Please select the project which you like to know about',
    (project_list[0], project_list[1], project_list[2])
)

print(option)
user_input = st.text_input('Please enter the query about project',
                           placeholder='example: What are all pending development Jira task in our project')


if st.button('Get Answer'):
    if user_input:
        text = 'Querying info about ' + str(option) + ' ....'
        with st.spinner(text):
            project_data = utility_functions.get_project_meta_data(option)
            # Initialize custom pre-processor module
            pp = preprocessing.Preprocess()
            processed_project_meta_data = pp.pre_preprocess_text(project_data)
            processed_project_meta_data_str = ''.join(processed_project_meta_data)
            st.write(constants.base_prompt+processed_project_meta_data_str)
            # model_answer = model.answer(constants.base_prompt+processed_project_meta_data_str, user_input)
            # st.write(model_answer)
