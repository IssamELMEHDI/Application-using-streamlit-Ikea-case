import streamlit as st 
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import io
import warnings

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/ikea logo.png'
logo = Image.open(path_file)

ikea_store = os.getcwd() + '/images/ikea photo.jpg'
ikea = Image.open(ikea_store)

st.set_page_config(
    page_title='Ikea | DataSet',
    page_icon=logo,
    layout='wide'
)

st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> Ikea Application: DataSet',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

data = pd.read_csv(os.getcwd()+'/data/ikea.csv')
st.dataframe(data)