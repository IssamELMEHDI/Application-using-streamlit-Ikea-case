import streamlit as st 
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import io
import warnings

from ETL.Data import factTable,data

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

st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> IKEA DataSet',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

data = data

st.header('Dataset')

def visualDataFrame(df):
    options = st.multiselect(
        '',
        list(df.columns),list(df.columns))
    tab1, tab2, tab3, tab4 = st.tabs([":card_file_box: Data", "Types", 'NAN', 'Info'])
    with tab1:
        st.subheader("A tab with a data")
        st.dataframe(df[options])
    with tab2:
        st.subheader("Column type :")
        st.text(df[options].dtypes)
    with tab3:
        st.subheader("Null values :")
        st.text(df[options].isna().sum())
    with tab4:
        st.subheader('DataFrame Info')
        buffer = io.StringIO()
        df[options].info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    
visualDataFrame(data)

st.header('Dataset après ETL Process')
visualDataFrame(factTable(data))

