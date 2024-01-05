import duckdb
import streamlit as st 
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import io
import warnings
from ETL.Data import factTable,data
from utils.graphs import histogram,scatter,boxPlot,pie

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/ikea logo.png'
logo = Image.open(path_file)

ikea_store = os.getcwd() + '/images/ikea photo.jpg'
ikea = Image.open(ikea_store)

st.set_page_config(
    page_title='Ikea | Dashboard',
    page_icon=logo,
    layout='wide'
)

st.markdown('# <img src="https://raw.githubusercontent.com/IssamELMEHDI/Application-using-streamlit-Ikea-case/master/images/ikea%20logo.png" alt="Ikea Logo" width=100/> IKEA Dashboard',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
duckdb_connection = duckdb.connect()

data=factTable(data)

cols1=st.columns(3)
with cols1[0]:
    price=f'''
SELECT name AS Produits,price AS Price FROM data 
GROUP BY name , price
'''
    price_for_products=duckdb_connection.execute(price).df()
    histogram(x=price_for_products['Produits'],y=price_for_products['Price'],title='prix par produit')

    
#with cols1[1]:    
    #scatter()
with cols1[2]:
    price=f'''
SELECT name AS Produits, category AS Category FROM data 
GROUP BY name , category
'''
    name_category=duckdb_connection.execute(price).df()
    histogram(x=name_category['Category'],y=name_category['Produits'],title='Categorie des produits')

cols2=st.columns(2)
with cols2[0]:
    box=f'''
SELECT price AS prix, category AS Category FROM data 
GROUP BY price , category
'''
    price_for_category=duckdb_connection.execute(box).df()
    boxPlot(x=price_for_category['prix'],y=price_for_category['Category'],df=price_for_category)

with cols2[1]:
    sellabe_online_category_query=f"""
    SELECT sellable_online,category FROM data
    GROUP BY sellable_online,category
    """
    sellabe_online_category=duckdb_connection.execute(sellabe_online_category_query).df()
    pie(sellabe_online_category,'category','sellabe_online')