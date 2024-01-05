import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import altair as alt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def histogram(x,y,title):
    fig = go.Figure(
    data=[go.Bar(x=x,y=y)],
    layout_title_text=title
    )
    st.plotly_chart(fig,use_container_width=True)

def scatter(source,x,y,color,size):    # source notre data ,x variables et y , color and size des produits 
    c=(alt.Chart(source).mark_circle().encode(
    alt.X(x).scale(zero=False),
    alt.Y(y).scale(zero=False, padding=1),
    color=color,
    size=size
    ))
    st.altair_chart(c,use_container_width=True)

def boxPlot(df,y,x):
    fig = px.box(df,x=x, y=y)
    st.plotly_chart(fig,use_container_width=True)

#def pie(df,category):
#    category = category
#    color = ["#416D9D", "#674028", "#DEAC58"]
#    df = pd.DataFrame({'category': category, 'value': [75, 10, 15]})
#
#    c=(alt.Chart(df, width=150, height=150).mark_arc(outerRadius=80).encode(
#    alt.Theta('value:Q').scale(range=[2.356, 8.639]),
#    alt.Color('category:N')
#        .title(None)
#        .scale(domain=category, range=color)
#        .legend(orient='none', legendX=160, legendY=50),
#    order='value:Q'
#    ).configure_view(
#    strokeOpacity=0
#    ))
#    st.altair_chart(c,use_container_width=True)

def pie(df,nominal,quantitative):
    

    c=(alt.Chart(df).mark_arc(outerRadius=80).encode(
    alt.Theta(f'{quantitative}:Q').scale(range=[2.356, 8.639]),
    alt.Color(f'{nominal}:N')
        .title(None)
        .legend(orient='none', legendX=460, legendY=0),
    order=f'{quantitative}:Q'
    ).configure_view(
    strokeOpacity=0
    ))
    st.altair_chart(c,use_container_width=True)