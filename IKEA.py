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
    page_title='Ikea | Home',
    page_icon=logo,
    layout='wide'
)

st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> Ikea Application',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.image('images\ikea photo.jpg')



st.markdown("""
---

<div align="center">


Bienvenue sur le Portail d'Analyse IKEA, votre destination pour explorer et comprendre en profondeur les tendances et les dynamiques autour des produits IKEA. À travers des analyses approfondies et des dashboards interactifs, cette plateforme offre un aperçu captivant du comportement des consommateurs, des variations de prix, de la disponibilité en ligne, et bien plus encore.
  
---
### Realized by: Issam EL MEHDI
            
</div>""",unsafe_allow_html=True)


# test load

data_load=st.button('data load')
if data_load:
    Loads(factTable(df),'data/','ikeaLoad.csv').send_to_csv()



