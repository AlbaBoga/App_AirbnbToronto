#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt

import os
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# mapas interactivos
import folium
from folium.plugins import FastMarkerCluster
import geopandas as gpd
from branca.colormap import LinearColormap

#to make the plotly graphs
import plotly.graph_objs as go
import chart_studio.plotly as py
from plotly.offline import iplot, init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
import plotly.express as px

#text mining
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from wordcloud import WordCloud
import streamlit as st
from PIL import Image
import altair as alt
from streamlit_folium import st_folium
import nltk
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Conclusiones', page_icon='🌆', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

listings = pd.read_csv("data/listings_final.csv")

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#
st.sidebar.title('Menú 🐻')

pages=['Conclusiones', 'Resumen de los datos']

selected_page = st.sidebar.selectbox("Seleccione:", pages)

if selected_page=='Conclusiones':
    col1,col2,col3=st.columns(3)
    with col2:
        image2 = Image.open('img/waterfront.jpg')
        st.image(image2, width=800)

        st.title('Conclusiones')

        st.markdown("""
        Toronto no sólo ofrece variedad en intereses de ocio y cultura a la hora de pasar el tiempo durante tus vacaciones, sino que las diferentes ofertas de Airbnb permiten una gran flexibilidad a la hora de encontrar un alojamiento que satisfaga las diferentes necesidades de los turistas. Se concluye en este análisis de oportunidad que:
        * Airbnb no sólo proporciona oportunidad turística, sino que también hace sentir a los turistas como en casa.
        * Hay una gran demanda de alquiler de casas o apartamentos para dos o cuatro personas, en base al número de ofertas, por lo que podría ser un buen punto de partida.
        * Hay un mercado muy amplio independientemente de la zona, permitiendo abarcar un gran rango de precios para satisfaccer las necesidades de los turistas.
        * Se han encontrado posibles infringimientos de la normativa vigente, por lo que animo a las comunidades de vecinos a suplir esa carencia dentro del mercado.
        * Hay un número mínimo de ofertas con la insignia superanfitrión, por lo que su remedio proporcionaría no sólo seguridad en los turistas, sino también grandes beneficios para los interesados.
        """)

else:
    st.title('Resumen de los datos')

    link = '<iframe title="AIRBNBTORONTO" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=191c2593-4c17-48a7-9b56-a1d00db5ae7c&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64" frameborder="0" allowFullScreen="true"></iframe>'

    st.markdown(link, unsafe_allow_html=True)



#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#