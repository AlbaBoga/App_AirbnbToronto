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
from streamlit_folium import st_folium
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Análisis de ofertas', page_icon='🌆', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

listings = pd.read_csv("data/listings_final.csv")

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#



st.title('Análisis de las ofertas de Airbnb en Toronto')

#---------------------------------------------------------------VECINDARIO---------------------------------------------------------------#
st.subheader('Vecindario')
st.markdown("""
Para satisfacer todas las necesidades de la ciudad, Toronto se divide en seis áreas diferentes que contaban con un total de 140 barrios desde finales de 1990 hasta marzo de 2020. En la actualidad Toronto cuenta con un total de 158 barrios, que intentan encapsular las diferentes culturas o etnias, las diferencias económicas y las diferentes necesidades culturales de la ciudad.

Entre las diferentes ofertas de Airbnb, primero se va a explorar cómo se encuentran divididas según la zona y finalmente, según los diferentes barrios.

Info: https://www.toronto.ca/city-government/data-research-maps/neighbourhoods-communities/neighbourhood-profiles/about-toronto-neighbourhoods/

En el siguiente mapa se puede observar la distribución de las ofertas por zonas y vecindarios.
""")
col1,col2,col3 = st.columns(3)
with col2:
    lats2018 = listings['latitude'].tolist()
    lons2018 = listings['longitude'].tolist()
    locations = list(zip(lats2018, lons2018))

    map1 = folium.Map(location=[43.651070, -79.347015], zoom_start=11.5)
    FastMarkerCluster(data=locations).add_to(map1)
    st_data = st_folium(map1, width=725)

st.markdown("""
##### Ofertas de Airbnb por área

Las principales zonas en las que se dividen los diferentes barrios de la ciudad de Toronto son Toronto, East York, North York, Etibicoke, York y Scarborough.

De las diferentes áreas, la zona de Toronto es donde se encuentra el centro de la ciudad y está compuesta por los barrios más antiguos, con arquitectura de gran importancia histórica.
""")

col1,col2,col3 = st.columns(3)
with col2:
    image2 = Image.open('img/districts.png')
    st.image(image2, width=600)

tab1, tab2 = st.tabs(['Número de ofertas', 'Precio total por estancia'])

with tab1:
    col1,col2,col3 = st.columns(3)
    with col1:
        numero_d=listings['District'].value_counts().sort_values(ascending=False).reset_index()
        numero_d['percent']=None
        for i in numero_d.index:
            numero_d.loc[i,'percent']=(numero_d.loc[i,'count']*100)/numero_d['count'].sum()
        numero_d['percent']=numero_d['percent'].apply(lambda x: np.round(x,2))
        st.write(numero_d)
    with col2:
        numero_d=listings['District'].value_counts().sort_values(ascending=True).reset_index()
        fig=px.bar(x=numero_d['count'], y=numero_d['District'], orientation='h', color=numero_d['District'],title = "Número de ofertas por área", template= "plotly_dark", color_discrete_sequence=['#3944BC','#757C88','#281E5D','#1520A6','#022D36','#1F456E'])
        fig.update_layout(
            xaxis_title="Número de ofertas",
            yaxis_title="Área"
        )
        st.plotly_chart(fig)

with tab2:
    col1,col2,col3 = st.columns(3)
    with col1:
        avg_price_d=listings.groupby('District')[['price','minimum_nights']].mean().sort_values(by='price', ascending=False).reset_index()
        avg_price_d['total_price']=None
        for i in avg_price_d.index:
            avg_price_d.loc[i,'total_price']=avg_price_d.loc[i,'price']*np.ceil(avg_price_d.loc[i,'minimum_nights'])

        avg_price_d['minimum_nights']=avg_price_d['minimum_nights'].apply(lambda x: np.ceil(x))
        avg_price_d['price']=avg_price_d['price'].apply(lambda x: np.round(x,2))
        avg_price_d['total_price']=avg_price_d['total_price'].apply(lambda x: np.round(x,2))
        st.write(avg_price_d)
    with col2:
        avg_price_d=avg_price_d.sort_values(by='total_price', ascending=True)
        fig = px.line(avg_price_d, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
        fig.add_bar(x=avg_price_d['District'], y=avg_price_d['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
        fig.update_layout(
            yaxis_title="Precio mínimo",
            xaxis_title="Área",
        )
        st.plotly_chart(fig)

st.markdown("""
Se comprueba que en la zona de Toronto es donde se concentran el mayor número de ofertas con casi el 70% de las ofertas totales, lo cual es de gran interés debido a su importancia turística. Por otro lado, con apenas el 1% de las ofertas, East York se colocaría en último puesto, siendo una zona de poco interés turístico, ya que es una zona mayormente residencial, para clase media y clase trabajadora.

Si se observa la media de precios por día por la media de noches mínimas de las ofertas, se puede ver que los precios más altos se pagan en la zona de Toronto, lo que parece indicar que la diferencia de precio diario entre ofertas es muy grande. Mientras que para el resto de zonas, el precio medio por estancia no varía en gran cantidad, sí que se observa una gran diferencia con respecto a Scarborough, que tiene el precio medio por estancia más bajo. En esta zona es donde se encontraría el Lago de Ontario, y aunque pueda no ser de interés debido a no ser céntrica, sigue siendo muy popular, concentrándose casi el 8% de las ofertas totales, gracias a sus paisajes únicos.

Info: https://familypedia.fandom.com/wiki/Scarborough,_Toronto

""")

st.markdown("""
##### Ofertas de Airbnb por barrio

Debido a que se ha obtenido un listado de las ofertas de Airbnb para los 140 barrios de la ciudad de Toronto, sólo se van a analizar la distribución de las ofertas en aquellos de interés, para facilitar la visualización.
""")

tab1, tab2, tab3, tab4 = st.tabs(['Barrios con más ofertas', 'Barrios con menos ofertas','Barrios más caros','Barrios más baratos'])

with tab1:
    col1,col2,col3 = st.columns(3)
    with col1:
        numero_v=listings.groupby('District')['neighbourhood'].value_counts().sort_values(ascending=False).reset_index()
        numero_v['percent']=None
        for i in numero_v.index:
            numero_v.loc[i,'percent']=(numero_v.loc[i,'count']*100)/numero_v['count'].sum()
            
        numero_v['percent']=numero_v['percent'].apply(lambda x: np.round(x,2))
        
        st.write(numero_v.head())
    with col2:
        numero_v_top5=numero_v[:5].copy().sort_values(by='count',ascending=True)
        fig=px.bar(x=numero_v_top5['count'], y=numero_v_top5['neighbourhood'], orientation='h', color=numero_v_top5['District'],title = "Número de ofertas por vecindario", template= "plotly_dark",color_discrete_sequence=['#3944BC','#757C88','#281E5D','#1520A6','#022D36','#1F456E'])
        fig.update_layout(
            xaxis_title="Número de ofertas",
            yaxis_title="Vecindarios con más ofertas"
        )
        st.plotly_chart(fig)

with tab2:
    col1,col2,col3 = st.columns(3)
    with col1:
        numero_v=listings.groupby('District')['neighbourhood'].value_counts().sort_values(ascending=False).reset_index()
        numero_v['percent']=None
        for i in numero_v.index:
            numero_v.loc[i,'percent']=(numero_v.loc[i,'count']*100)/numero_v['count'].sum()
            
        numero_v['percent']=numero_v['percent'].apply(lambda x: np.round(x,2))
        
        st.write(numero_v.tail())
    with col2:
        numero_v_least5=numero_v[-5:].copy().sort_values(by='count',ascending=False)
        fig=px.bar(x=numero_v_least5['count'], y=numero_v_least5['neighbourhood'], orientation='h', color=numero_v_least5['District'],title = "Número de ofertas por vecindario", template= "plotly_dark", color_discrete_sequence=['#3944BC','#757C88','#281E5D','#1520A6','#022D36','#1F456E'])
        fig.update_layout(
            xaxis_title="Número de ofertas",
            yaxis_title="Vecindarios con menos ofertas"
        )
        st.plotly_chart(fig)

with tab3:
    col1,col2,col3 = st.columns(3)
    with col1:
        avg_price_v=listings.groupby(['District','neighbourhood'])[['price','minimum_nights']].mean().sort_values(by='price', ascending=False).reset_index()
        avg_price_v['total_price']=None
        for i in avg_price_v.index:
            avg_price_v.loc[i,'total_price']=avg_price_v.loc[i,'price']*np.ceil(avg_price_v.loc[i,'minimum_nights'])

        avg_price_v['minimum_nights']=avg_price_v['minimum_nights'].apply(lambda x: int(np.ceil(x)))
        avg_price_v['price']=avg_price_v['price'].apply(lambda x: np.round(x,2))
        avg_price_v['total_price']=avg_price_v['total_price'].apply(lambda x: np.round(x,2))
        
        st.write(avg_price_v.head())
    with col2:
        avg_price_v_top5=avg_price_v[:5].copy().sort_values(by='total_price',ascending=False)
        fig=px.bar(x=avg_price_v_top5['total_price'], y=avg_price_v_top5['neighbourhood'], orientation='h', color=avg_price_v_top5['District'],title = "Precio total medio de ofertas por vecindario", template= "plotly_dark",color_discrete_sequence=['#3944BC','#757C88','#281E5D','#1520A6','#022D36','#1F456E'],  hover_data={'Promedio precio': avg_price_v_top5['price'], 'Noches mínimas': avg_price_v_top5['minimum_nights']})
        fig.update_layout(
            xaxis_title="Precio mínimo total",
            yaxis_title="Vecindarios más caros"
        )
        st.plotly_chart(fig)

with tab4:
    col1,col2,col3 = st.columns(3)
    with col1:
        avg_price_v=listings.groupby(['District','neighbourhood'])[['price','minimum_nights']].mean().sort_values(by='price', ascending=False).reset_index()
        avg_price_v['total_price']=None
        for i in avg_price_v.index:
            avg_price_v.loc[i,'total_price']=avg_price_v.loc[i,'price']*np.ceil(avg_price_v.loc[i,'minimum_nights'])

        avg_price_v['minimum_nights']=avg_price_v['minimum_nights'].apply(lambda x: int(np.ceil(x)))
        avg_price_v['price']=avg_price_v['price'].apply(lambda x: np.round(x,2))
        avg_price_v['total_price']=avg_price_v['total_price'].apply(lambda x: np.round(x,2))
        
        st.write(avg_price_v.tail())
    with col2:
        avg_price_v_least5=avg_price_v[-5:].copy().sort_values(by='total_price',ascending=False)
        fig=px.bar(x=avg_price_v_least5['total_price'], y=avg_price_v_least5['neighbourhood'], orientation='h', color=avg_price_v_least5['District'],title = "Precio total medio de ofertas por vecindario", template= "plotly_dark", color_discrete_sequence=['#3944BC','#757C88','#281E5D','#1520A6','#022D36','#1F456E'],  hover_data={'Promedio precio': avg_price_v_top5['price'], 'Noches mínimas': avg_price_v_top5['minimum_nights']})
        fig.update_layout(
            xaxis_title="Precio mínimo total",
            yaxis_title="Vecindarios más baratos"
        )
        st.plotly_chart(fig)

st.markdown("""
La zona donde se concentran el mayor número de ofertas por barrio sigue siendo en la zona de Toronto, de la cual, el barrio de Waterfront Communities-The Island tiene casi un 20% de ellas. Para el resto de barrios, el número de ofertas baja considerablemente comprendiendo el 4% y el 0.01% de las ofertas para los 139 barrios restantes. Waterfront Communities-The Island es una zona céntrica que comprende 43 km y donde se concentra la zona comercial y edificios de oficinas. Es un sitio de gran interés turístico ya que es donde se encuentra la Torre CN y está a tan sólo dos horas en coche de las cataratas del Niágara, la segunda zona con el mayor número de ofertas.

Si observamos el precio total medio por estancia, se observa que, en la zona de Toronto, más concretamente en el barrio Roncesvalles es donde se ofrecen los alquileres medios más caros, debido a que es una zona residencial con casas de arquitectura victoriana con más de cien años de antiguedad renovadas. Además, es una zona de gran interés turístico, no sólo por su arquitectura, sino por los diferentes sitios de ocio y restaurantes que ofrece. Finalmente, entre las zonas donde se ofrecerían los precios medios más baratos por estancia, predomina la zona de North York. Más concretamente, Glenfield Jane Heights que es un barrio residencial donde el 60% de los residentes son inmigrantes.

Info: https://storymaps.arcgis.com/stories/b5c41034bd714a00b4836e41bc440fdf

https://www.lifewest.ca/roncesvalles-village

https://www.realosophy.com/glenfield-jane-heights-toronto/neighbourhood-profile

""")

#---------------------------------------------------------------VECINDARIO---------------------------------------------------------------#



#---------------------------------------------------------------PROPIEDAD Y HABITACIÓN---------------------------------------------------------------#
st.subheader('Según el tipo de propiedad y habitación')


st.markdown("""
##### Ofertas de Airbnb por tipo de habitación
Se ofrecen diferentes tipos de habitaciones según las necesidades de los invitados. Para aquellos que están buscando un mayor nivel de intimidad, se ofrece el alquiler de apartamentos o casas en su totalidad. Para aquellos a los que no les importa vivir con los locales y prefieren experimentar la vida en Toronto de primera mano, se ofrece la opción de habitaciones privadas o compartidas en residencias locales. Para concluir, también se ofrece la llamada estancia en habitación de hotel, de la cual sólo se han encontrado tres ofertas, una de ellas sin información acerca de su precio.
""")
col1,col2,col3 = st.columns(3)
with col2:
    fig=px.scatter_mapbox(listings, lat='latitude', lon='longitude', size='price', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas por tipo de habitación en Toronto', template= "plotly_dark", size_max=20, animation_frame='room_type',color_discrete_sequence=['#274490'])
    st.plotly_chart(fig)

tab1, tab2 = st.tabs(['Número de ofertas', 'Precio total por estancia'])

with tab1:
    col1,col2,col3 = st.columns(3)
    with col2:
        numero_room_d=listings.groupby('District')['room_type']. value_counts().sort_values(ascending=False).reset_index()
        numero_room_d['percent']=None
        for i in numero_room_d.index:
            numero_room_d.loc[i,'percent']=(numero_room_d.loc[i,'count']*100)/numero_room_d['count'].sum()
        numero_room_d['percent']=numero_room_d['percent'].apply(lambda x: np.round(x,2))


        fig=px.bar(x=numero_room_d['percent'], y=numero_room_d['District'], color=numero_room_d['room_type'],title = "Tipo de habitaciones por área", template= "plotly_dark",barmode='group',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])
        fig.update_layout(
            xaxis_title="Promedio de tipo de habitaciones",
            yaxis_title="Área"
        )
        st.plotly_chart(fig)

with tab2:
    col1,col2,col3 = st.columns(3)
    with col2:
        avg_price_r_d=listings.groupby(['District','room_type'])[['price','minimum_nights']].mean().sort_values(by='price', ascending=False).reset_index()
        avg_price_r_d['total_price']=None
        for i in avg_price_r_d.index:
            avg_price_r_d.loc[i,'total_price']=avg_price_r_d.loc[i,'price']*np.ceil(avg_price_r_d.loc[i,'minimum_nights'])

        avg_price_r_d['minimum_nights']=avg_price_r_d['minimum_nights'].apply(lambda x: int(np.ceil(x)))
        avg_price_r_d['price']=avg_price_r_d['price'].apply(lambda x: np.round(x,2))
        avg_price_r_d['total_price']=avg_price_r_d['total_price'].apply(lambda x: np.round(x,2))

        
        fig = px.scatter(data_frame=avg_price_r_d, y='total_price', x='District', size='total_price', color='room_type', hover_data=['room_type','price','minimum_nights'], log_x=False,size_max=60,title="Precio total medio de tipo de habitación por área",template="plotly_dark",color_discrete_sequence=['#59788E','#960018','#D9381E','#3944BC'])
        fig.update_layout(
            yaxis_title="Precio mínimo total",
            xaxis_title="Área"
        )
        st.plotly_chart(fig)

st.markdown("""
Se observa que casi el 60% de las ofertas van dirigidas a turistas que busquen alquilar un apartamento o una casa, con un precio medio de estancia que va de los 4000 a los 6700 dólares canadienses, siendo la oferta más cara, y cuyo precio cambia según la zona. Para los demás casos, a pesar de que la zona de Toronto sigue siendo la más cara, los precios medios por estancia se mantienen, encontrando el precio mínimo en la zona de Scaraborough, para una habitación compartida.
""")

st.markdown("""
##### Ofertas de Airbnb por tipo de propiedad
Para los tipos de propiedades ofrecidos se encuentra una gran variedad, desde alquiler de estudios, villas o plantas de edificios. Por ello, se van a mirar aquellas ofertas más populares según el tipo de propiedad, ya que se han encontrado casi 190 tipos diferentes.
""")
col1,col2,col3 = st.columns(3)
with col2:
    fig=px.scatter_mapbox(listings, lat='latitude', lon='longitude', size='price', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas por tipo de propiedad en Toronto', template= "plotly_dark", size_max=80, animation_frame='property_type',color_discrete_sequence=['#274490'])
    st.plotly_chart(fig)

    numero_prop_d=listings.groupby(['District','room_type'])['property_type']. value_counts().sort_values(ascending=False).reset_index()
    numero_prop_d['percent']=None
    for i in numero_prop_d.index:
        numero_prop_d.loc[i,'percent']=(numero_prop_d.loc[i,'count']*100)/numero_prop_d['count'].sum()
    numero_prop_d['percent']=numero_prop_d['percent'].apply(lambda x: np.round(x,2))

    numero_prop_d_top5 = numero_prop_d.groupby('District').apply(lambda x: x.nlargest(5, 'percent')).reset_index(drop=True)

    fig=px.bar(x=numero_prop_d_top5['percent'], y=numero_prop_d_top5['District'], color=numero_prop_d_top5['property_type'],title = "Tipo de propiedad por área (Top 5)", template= "plotly_dark",barmode='group',color_discrete_sequence=['#B22222','#281E5D','#757C88','#D21F3C','#022D36','#D9381E','#1F456E'])
    fig.update_layout(
        xaxis_title="Promedio de tipo de propiedad",
        yaxis_title="Área"
    )
    st.plotly_chart(fig)

st.markdown("""
En la zona de Toronto, casi el 50% de las ofertas según el tipo de propiedad van centradas al alquiler de apartamentos, mientras que para el resto de zonas también son muy populares el alquiler de habitaciones privadas o compartidas en casas, apartamentos alquilados o zonas de camping.
""")

#---------------------------------------------------------------PROPIEDAD Y HABITACIÓN---------------------------------------------------------------#



#---------------------------------------------------------------PERSONAS MÁXIMAS---------------------------------------------------------------#
st.subheader('Número máximo de personas por oferta')


st.markdown("""
El tercer y último punto de interés sería el número de personas que pueden albergar las diferentes ofertas y aquellos que son más populares entre las mismas.
""")

tab1, tab2 = st.tabs(['Número máximo de personas por oferta', 'Número máximo por zonas'])

with tab1:
    col1,col2,col3 = st.columns(3)
    with col2:
        feq=listings['accommodates'].value_counts().sort_index()
        fig=px.bar(feq,title= "Número máximo de personas por oferta en Toronto",template= "plotly_dark", labels=dict(index="Número máximo de personas",value="Número de ofertas"), width = 1000,color_discrete_sequence=['#274490'])
        st.plotly_chart(fig)

with tab2:
    col1,col2,col3 = st.columns(3)
    with col2:
        numero_peeps_d=listings.groupby('District')['accommodates'].value_counts().reset_index()
        
        fig = px.scatter(numero_peeps_d, x="accommodates", y="count", color="District",  size="count", hover_data=['accommodates'], log_x=False, size_max=60, template='plotly_dark',title='Número máximo de personas por oferta y área',color_discrete_sequence=['#B22222','#281E5D','#757C88','#D21F3C','#022D36','#274490','#1F456E'])
        fig.update_layout(
            yaxis_title="Número de ofertas",
            xaxis_title="Número máximo de personas"
        )
        st.plotly_chart(fig)

st.markdown("""
El número de personas a quienes están destinados estos alquileres va desde 1 a 16 personas, siendo los más populares aquellos alquileres para 2 o 4 personas, lo que quiere indicar que las ofertas se centran en parejas o pequeñas familias, siendo la zona de Toronto la que mayor número de ofertas ofrece a 2 personas, con un total de casi 5000 ofertas diferentes.
""")

#---------------------------------------------------------------PERSONAS MÁXIMAS---------------------------------------------------------------#



#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#