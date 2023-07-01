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


#to make the plotly graphs
import plotly.graph_objs as go

import plotly.express as px


import streamlit as st
from PIL import Image

from streamlit_folium import st_folium

#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Turismo en Toronto', page_icon='🌆', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

listings = pd.read_csv("data/listings_final.csv")

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#



#--------------------------------------TÍTULO-------------------------------------#
st.sidebar.title('Menú 🐻')
st.title('Evaluación del Turismo en la ciudad de Toronto')
st.markdown(
            """
Para poder comparar la calidad de los alojamientos, se va a utilizar aquellas ofertas mayoritarias, que son las que van dirigidas al mayor número de turistas. Por ello, en este apartado se van a comparar los precios y las reseñas destinadas a dos personas, que era el número de personas a quienes más ofertas iban dirigidas, según las diferentes zonas.
        """
        )

#--------------------------------------TÍTULO-------------------------------------#



#--------------------------------------PRECIO MEDIO DIARIO POR ÁREA-------------------------------------#

st.subheader('Precio medio diario por área')

pages=['Toronto', 'East York', 'North York', 'Etobicoke', 'York', 'Scarborough']

selected_page = st.sidebar.selectbox("Distribución de precio por zona", pages)



if selected_page == 'Toronto':
    tab1, tab2 = st.tabs(['Distribución de precio en zona Toronto', 'Precio medio diario por zona'])
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq1 = listings[(listings['accommodates']==2)&(listings['District']=='Toronto')]
            fig=px.histogram(feq1, x='price',color_discrete_sequence=['#274490'])
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq = listings[listings['accommodates']==2]
            feq = feq.groupby('District')[['price','minimum_nights']].mean().reset_index().sort_values(by='price',ascending=True)
            feq['total_price']=None
            for i in feq.index:
                feq.loc[i,'total_price']=feq.loc[i,'price']*np.ceil(feq.loc[i,'minimum_nights'])

            feq['minimum_nights']=feq['minimum_nights'].apply(lambda x: np.ceil(x))
            feq['price']=feq['price'].apply(lambda x: np.round(x,2))
            feq['total_price']=feq['total_price'].apply(lambda x: np.round(x,2))

            feq=feq.sort_values(by='total_price', ascending=True)
            fig = px.line(feq, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
            fig.add_bar(x=feq['District'], y=feq['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
            fig.update_layout(
                yaxis_title="Precio mínimo",
                xaxis_title="Área",
            )
            st.plotly_chart(fig)

    
elif selected_page == 'East York':
    tab1, tab2 = st.tabs(['Distribución de precio en zona East York', 'Precio medio diario por zona'])
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq1 = listings[(listings['accommodates']==2)&(listings['District']=='East York')]
            fig=px.histogram(feq1, x='price',color_discrete_sequence=['#274490'])
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq = listings[listings['accommodates']==2]
            feq = feq.groupby('District')[['price','minimum_nights']].mean().reset_index().sort_values(by='price',ascending=True)
            feq['total_price']=None
            for i in feq.index:
                feq.loc[i,'total_price']=feq.loc[i,'price']*np.ceil(feq.loc[i,'minimum_nights'])

            feq['minimum_nights']=feq['minimum_nights'].apply(lambda x: np.ceil(x))
            feq['price']=feq['price'].apply(lambda x: np.round(x,2))
            feq['total_price']=feq['total_price'].apply(lambda x: np.round(x,2))

            feq=feq.sort_values(by='total_price', ascending=True)
            fig = px.line(feq, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
            fig.add_bar(x=feq['District'], y=feq['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
            fig.update_layout(
                yaxis_title="Precio mínimo",
                xaxis_title="Área",
            )
            st.plotly_chart(fig)

elif selected_page == 'North York':
    tab1, tab2 = st.tabs(['Distribución de precio en zona North York', 'Precio medio diario por zona'])
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq1 = listings[(listings['accommodates']==2)&(listings['District']=='North York')]
            fig=px.histogram(feq1, x='price',color_discrete_sequence=['#274490'])
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq = listings[listings['accommodates']==2]
            feq = feq.groupby('District')[['price','minimum_nights']].mean().reset_index().sort_values(by='price',ascending=True)
            feq['total_price']=None
            for i in feq.index:
                feq.loc[i,'total_price']=feq.loc[i,'price']*np.ceil(feq.loc[i,'minimum_nights'])

            feq['minimum_nights']=feq['minimum_nights'].apply(lambda x: np.ceil(x))
            feq['price']=feq['price'].apply(lambda x: np.round(x,2))
            feq['total_price']=feq['total_price'].apply(lambda x: np.round(x,2))

            feq=feq.sort_values(by='total_price', ascending=True)
            fig = px.line(feq, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
            fig.add_bar(x=feq['District'], y=feq['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
            fig.update_layout(
                yaxis_title="Precio mínimo",
                xaxis_title="Área",
            )
            st.plotly_chart(fig)

elif selected_page == 'Etobicoke':
    tab1, tab2 = st.tabs(['Distribución de precio en zona Etobicoke', 'Precio medio diario por zona'])
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq1 = listings[(listings['accommodates']==2)&(listings['District']=='Etobicoke')]
            fig=px.histogram(feq1, x='price',color_discrete_sequence=['#274490'])
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq = listings[listings['accommodates']==2]
            feq = feq.groupby('District')[['price','minimum_nights']].mean().reset_index().sort_values(by='price',ascending=True)
            feq['total_price']=None
            for i in feq.index:
                feq.loc[i,'total_price']=feq.loc[i,'price']*np.ceil(feq.loc[i,'minimum_nights'])

            feq['minimum_nights']=feq['minimum_nights'].apply(lambda x: np.ceil(x))
            feq['price']=feq['price'].apply(lambda x: np.round(x,2))
            feq['total_price']=feq['total_price'].apply(lambda x: np.round(x,2))

            feq=feq.sort_values(by='total_price', ascending=True)
            fig = px.line(feq, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
            fig.add_bar(x=feq['District'], y=feq['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
            fig.update_layout(
                yaxis_title="Precio mínimo",
                xaxis_title="Área",
            )
            st.plotly_chart(fig)

elif selected_page == 'York':
    tab1, tab2 = st.tabs(['Distribución de precio en zona York', 'Precio medio diario por zona'])
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq1 = listings[(listings['accommodates']==2)&(listings['District']=='York')]
            fig=px.histogram(feq1, x='price',color_discrete_sequence=['#274490'])
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq = listings[listings['accommodates']==2]
            feq = feq.groupby('District')[['price','minimum_nights']].mean().reset_index().sort_values(by='price',ascending=True)
            feq['total_price']=None
            for i in feq.index:
                feq.loc[i,'total_price']=feq.loc[i,'price']*np.ceil(feq.loc[i,'minimum_nights'])

            feq['minimum_nights']=feq['minimum_nights'].apply(lambda x: np.ceil(x))
            feq['price']=feq['price'].apply(lambda x: np.round(x,2))
            feq['total_price']=feq['total_price'].apply(lambda x: np.round(x,2))

            feq=feq.sort_values(by='total_price', ascending=True)
            fig = px.line(feq, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
            fig.add_bar(x=feq['District'], y=feq['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
            fig.update_layout(
                yaxis_title="Precio mínimo",
                xaxis_title="Área",
            )
            st.plotly_chart(fig)

elif selected_page == 'Scarborough':
    tab1, tab2 = st.tabs(['Distribución de precio en zona Scarborough', 'Precio medio diario por zona'])
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq1 = listings[(listings['accommodates']==2)&(listings['District']=='Scarborough')]
            fig=px.histogram(feq1, x='price',color_discrete_sequence=['#274490'])
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq = listings[listings['accommodates']==2]
            feq = feq.groupby('District')[['price','minimum_nights']].mean().reset_index().sort_values(by='price',ascending=True)
            feq['total_price']=None
            for i in feq.index:
                feq.loc[i,'total_price']=feq.loc[i,'price']*np.ceil(feq.loc[i,'minimum_nights'])

            feq['minimum_nights']=feq['minimum_nights'].apply(lambda x: np.ceil(x))
            feq['price']=feq['price'].apply(lambda x: np.round(x,2))
            feq['total_price']=feq['total_price'].apply(lambda x: np.round(x,2))

            feq=feq.sort_values(by='total_price', ascending=True)
            fig = px.line(feq, x='District', y="minimum_nights", hover_data=['total_price'], template= "plotly_dark", title = "Precio total medio por área en Toronto")
            fig.add_bar(x=feq['District'], y=feq['price'], name='Promedio precio mínimo', marker_color=['#B22222','#960018','#8D021F','#D21F3C','#722F37','#D9381E'])
            fig.update_layout(
                yaxis_title="Precio mínimo",
                xaxis_title="Área",
            )
            st.plotly_chart(fig)

st.markdown("""
    De las diferentes zonas, la de Toronto es la que ofrece el mayor rango de precios diarios para dos personas. La mayoría de ofertas se concentran entre los 50 y 200 dólares canadienses. 
    
    También, se aprecia en las diferentes distribuciones que existe una catidad considerable de valores atípicos dependiendo de la zona. Estos valores se pueden explicar a través de las grandes diferencias de precio vistas en el análisis primario de las ofertas, donde se veían precios muy altos para aquellas zonas con importancia histórica.

    Si se comprueban los precios diarios medios para todas las zonas, en alojamientos de dos personas, se puede ver que la zona de Toronto es la más cara, seguida por York. Esto se debe a que, a pesar de que la mayoría de ofertas rondan el mismo precio medio diario, los valores atípicos dentro de cada zona elevan considerablemente la media final de dichos precios.

    """)
#--------------------------------------PRECIO MEDIO DIARIO POR ÁREA-------------------------------------#



#--------------------------------------PRECIO MEDIO DIARIO POR VECINDARIO-------------------------------------#

st.subheader('Precio medio diario por barrio')

adam = gpd.read_file("data/neighbourhoods.geojson")
adam['neighbourhood']=adam['neighbourhood'].str.lower().str.replace("[-|'|/|.]", ' ',regex=True)
adam['neighbourhood']=adam['neighbourhood'].str.title()
feq = listings[listings['accommodates']==2]
feq = feq.groupby('neighbourhood')['price'].mean().reset_index()
#feq = feq.transpose()
adam = pd.merge(adam, feq, on='neighbourhood', how='left')
adam.rename(columns={'price': 'average_price'}, inplace=True)
adam.average_price = adam.average_price.round(decimals=0)

map_dict = adam.set_index('neighbourhood')['average_price'].to_dict()
color_scale = LinearColormap(['blue','red'], vmin = min(map_dict.values()), vmax = max(map_dict.values()))

def get_color(feature):
    value = map_dict.get(feature['properties']['neighbourhood'])
    return color_scale(value)

map3 = folium.Map(location=[43.651070, -79.347015], zoom_start=11)
folium.GeoJson(data=adam,
               name='Toronto',
               tooltip=folium.features.GeoJsonTooltip(fields=['neighbourhood', 'average_price'],
                                                      labels=True,
                                                      sticky=False),
               style_function= lambda feature: {
                   'fillColor': get_color(feature),
                   'color': 'black',
                   'weight': 1,
                   'dashArray': '5, 5',
                   'fillOpacity':0.5
                   },
               highlight_function=lambda feature: {'weight':3, 'fillColor': get_color(feature), 'fillOpacity': 0.8}).add_to(map3)
col1,col2,col3 = st.columns(3)
with col2:
    st_data = st_folium(map3, width=725)

st.markdown("""
En esta gráfica se comprueban los precios medios diarios para alojamientos de dos personas. Se puede ver que los precios más caros están repartidos por las diferentes zonas de la ciudad de Toronto. No obstante, la zona de Toronto es donde se concentran, no sólo el mayor número de ofertas, sino también los precios más caros, sobre todo en la zona céntrica de la ciudad.
""")

#--------------------------------------PRECIO MEDIO DIARIO POR VECINDARIO-------------------------------------#



#--------------------------------------OPINIONES PRINCIPALES POR ÁREA-------------------------------------#
st.subheader('Opiniones principales')

st.markdown("""
##### Promedio de opiniones por área
""")
col1,col2,col3 = st.columns(3)
with col2:
    feq = listings[(listings['number_of_reviews'] >= 10) & (listings['accommodates'] == 2)]
    feq1 = feq.groupby('District')['review_scores_location'].mean().sort_values(ascending=False)
    feq1=feq1.reset_index()
    
    fig = px.bar(feq1, x='review_scores_location', y='District', orientation='h', color='District', width=800, height=400,template='plotly_dark', color_discrete_sequence=['#3944BC','#757C88','#281E5D','#1520A6','#022D36','#1F456E'])

    fig.update_layout(
        title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
        xaxis_title="Puntuación (hasta 5 estrellas)",
        yaxis_title="Zona",
    )
    st.plotly_chart(fig)



pages=['Toronto', 'East York', 'North York', 'Etobicoke', 'York', 'Scarborough']

selected_page = st.sidebar.selectbox("Opiniones principales por zona", pages)

if selected_page == 'Toronto':
    st.markdown("""
##### Opiniones principales para zona Toronto
""")
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Localización','Limpieza','Calidad-Precio','Comunicación','Bienvenida','Realismo'])

    listings1 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='Toronto')&(listings['accommodates']==2)]
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['review_scores_location'].value_counts().sort_index()
            feq=feq.reset_index()

            # -- #
            feq1 = feq['review_scores_location'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_location'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_location'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_location', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación localización (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['review_scores_cleanliness'].value_counts().sort_index()
            feq=feq.reset_index()

            # -- #
            feq1 = feq['review_scores_cleanliness'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_cleanliness'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_cleanliness'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_cleanliness', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Limpieza (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab3:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['review_scores_value'].value_counts().sort_index()
            feq=feq.reset_index()

            # -- #
            feq1 = feq['review_scores_value'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_value'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_value'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_value', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Calidad-Precio (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab4:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['review_scores_communication'].value_counts().sort_index()
            feq=feq.reset_index()

            # -- #
            feq1 = feq['review_scores_communication'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_communication'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_communication'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_communication', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Comunicación (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab5:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['review_scores_checkin'].value_counts().sort_index()
            feq=feq.reset_index()

            # -- #
            feq1 = feq['review_scores_checkin'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_checkin'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_checkin'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_checkin', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Bienvenida (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab6:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['review_scores_accuracy'].value_counts().sort_index()
            feq=feq.reset_index()

            # -- #
            feq1 = feq['review_scores_accuracy'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_accuracy'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_accuracy'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_accuracy', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Realismo (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)



elif selected_page == 'East York':
    st.markdown("""
##### Opiniones principales para zona East York
""")
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Localización','Limpieza','Calidad-Precio','Comunicación','Bienvenida','Realismo'])

    listings2 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='East York')&(listings['accommodates']==2)]
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['review_scores_location'].value_counts().sort_index()
            feq=feq.reset_index()

	# -- #
            feq1 = feq['review_scores_location'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_location'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_location'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_location', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación localización (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['review_scores_cleanliness'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_cleanliness'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_cleanliness'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_cleanliness'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_cleanliness', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Limpieza (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab3:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['review_scores_value'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_value'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_value'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_value'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_value', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Calidad-Precio (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab4:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['review_scores_communication'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_communication'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_communication'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_communication'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_communication', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Comunicación (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab5:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['review_scores_checkin'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_checkin'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_checkin'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_checkin'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_checkin', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Bienvenida (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab6:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['review_scores_accuracy'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_accuracy'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_accuracy'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_accuracy'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_accuracy', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Realismo (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

elif selected_page == 'North York':
    st.markdown("""
##### Opiniones principales para zona North York
""")
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Localización','Limpieza','Calidad-Precio','Comunicación','Bienvenida','Realismo'])

    listings3 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='North York')&(listings['accommodates']==2)]
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['review_scores_location'].value_counts().sort_index()
            feq=feq.reset_index()

	# -- #
            feq1 = feq['review_scores_location'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_location'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_location'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_location', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación localización (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['review_scores_cleanliness'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_cleanliness'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_cleanliness'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_cleanliness'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_cleanliness', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Limpieza (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab3:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['review_scores_value'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_value'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_value'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_value'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_value', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Calidad-Precio (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab4:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['review_scores_communication'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_communication'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_communication'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_communication'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_communication', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Comunicación (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab5:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['review_scores_checkin'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_checkin'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_checkin'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_checkin'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_checkin', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Bienvenida (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab6:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['review_scores_accuracy'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_accuracy'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_accuracy'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_accuracy'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_accuracy', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Realismo (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

elif selected_page == 'Etobicoke':
    st.markdown("""
##### Opiniones principales para zona Etobicoke
""")
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Localización','Limpieza','Calidad-Precio','Comunicación','Bienvenida','Realismo'])

    listings4 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='Etobicoke')&(listings['accommodates']==2)]
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['review_scores_location'].value_counts().sort_index()
            feq=feq.reset_index()

	# -- #
            feq1 = feq['review_scores_location'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_location'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_location'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_location', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación localización (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['review_scores_cleanliness'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_cleanliness'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_cleanliness'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_cleanliness'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_cleanliness', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Limpieza (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab3:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['review_scores_value'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_value'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_value'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_value'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_value', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Calidad-Precio (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab4:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['review_scores_communication'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_communication'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_communication'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_communication'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_communication', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Comunicación (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab5:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['review_scores_checkin'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_checkin'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_checkin'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_checkin'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_checkin', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Bienvenida (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab6:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['review_scores_accuracy'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_accuracy'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_accuracy'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_accuracy'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_accuracy', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Realismo (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

elif selected_page == 'York':
    st.markdown("""
##### Opiniones principales para zona York
""")
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Localización','Limpieza','Calidad-Precio','Comunicación','Bienvenida','Realismo'])

    listings5 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='York')&(listings['accommodates']==2)]
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['review_scores_location'].value_counts().sort_index()
            feq=feq.reset_index()

	# -- #
            feq1 = feq['review_scores_location'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_location'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_location'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_location', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación localización (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['review_scores_cleanliness'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_cleanliness'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_cleanliness'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_cleanliness'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_cleanliness', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Limpieza (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab3:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['review_scores_value'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_value'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_value'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_value'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_value', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Calidad-Precio (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab4:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['review_scores_communication'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_communication'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_communication'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_communication'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_communication', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Comunicación (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab5:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['review_scores_checkin'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_checkin'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_checkin'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_checkin'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_checkin', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Bienvenida (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab6:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['review_scores_accuracy'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_accuracy'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_accuracy'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_accuracy'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_accuracy', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Realismo (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

elif selected_page == 'Scarborough':
    st.markdown("""
##### Opiniones principales para zona Scarborough
""")
    tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Localización','Limpieza','Calidad-Precio','Comunicación','Bienvenida','Realismo'])

    listings6 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='Scarborough')&(listings['accommodates']==2)]
    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['review_scores_location'].value_counts().sort_index()
            feq=feq.reset_index()

	# -- #
            feq1 = feq['review_scores_location'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_location'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_location'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_location', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación localización (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab2:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['review_scores_cleanliness'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_cleanliness'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_cleanliness'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_cleanliness'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_cleanliness', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Limpieza (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab3:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['review_scores_value'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_value'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_value'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_value'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_value', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Calidad-Precio (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab4:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['review_scores_communication'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_communication'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_communication'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_communication'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_communication', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Comunicación (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab5:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['review_scores_checkin'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_checkin'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_checkin'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_checkin'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_checkin', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Bienvenida (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

    with tab6:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['review_scores_accuracy'].value_counts().sort_index()
            feq=feq.reset_index()

# -- #
            feq1 = feq['review_scores_accuracy'].copy()
            feq1=feq1.reset_index()
            
            feq1['NPS']=None
            
            for i in feq1.index:
                if feq1.loc[i, 'review_scores_accuracy'] <= 3.0:
                    feq1.loc[i, 'NPS'] = 'Detractor'
                elif 3.0 < feq1.loc[i, 'review_scores_accuracy'] <= 4.0:
                    feq1.loc[i, 'NPS'] = 'Passive'
                else:
                    feq1.loc[i, 'NPS'] = 'Promoter'
            
            x=feq1[feq1['NPS']=='Promoter'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            y=feq1[feq1['NPS']=='Detractor'].groupby('NPS')['NPS'].value_counts().reset_index()
            
            if x.empty:
                x.loc[0,'count']=0
            if y.empty:
                y.loc[0,'count']=0
            
            nps=((x['count']/len(feq1['NPS']))-(y['count']/len(feq1['NPS'])))*100
            nps=nps.reset_index()
            st.write('Net Promoter Score: ',np.round(nps.loc[0,'count'],2))
            # --- #

            fig = px.bar(feq, x='review_scores_accuracy', y='count', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Promedio de opiniones para alojamientos de 2 personas (mínimo 10 reviews)",
                xaxis_title="Puntuación Realismo (hasta 5 estrellas)",
                yaxis_title="Número de puntuaciones",
            )
            st.plotly_chart(fig)

st.markdown("""
    Se observa que la media de puntuaciones para las ofertas que tienen un mínimo de diez reseñas, dividas por zonas, para dos personas, son altamente positivas, superando el 4.5/5 en todos los casos, y siendo la zona de Toronto, la que tiene la mejor puntuación de todas.

    Para medir la satisfacción de los usuarios en función de las diferentes reseñas y las zonas, se ha utilizado la herramienta Net Promoter Score que muestra la satisfacción del cliente en base al score proporcionado. Como se comprueba, para todas las zonas hay un score por encima del 80%, lo que supone una valoración muy positiva de las ofertas.
    """)

#--------------------------------------OPINIONES PRINCIPALES POR ÁREA-------------------------------------#



#--------------------------------------SUPERANFITRIÓN-------------------------------------#
st.subheader('Superanfitriones de Airbnb')
st.markdown("""
Airbnb ofrece la oportunidad a sus anfitriones de convertirse en superanfitriones. Para ello, la empresa se asegura cada tres meses que los anfitriones participantes cumplen una serie de requisitos indispensables:
* Valoración mínima de 4.8/5
* Más de 10 estancias en el último año o 100 noches distribuidas en al menos 3 estancias.
* Índice de cancelación menor al 1%.
* Índice de respuesta del 90% en un plazo de 24 horas.

Este reconocimiento, además de ofrecer ventajas exclusivas, proporciona una seguridad añadida a aquellos nuevos turistas en busca de una buena experiencia durante su viaje.

Info: https://www.airbnb.es/d/superhost?_set_bev_on_new_domain=1687613627_NGQ1Y2E0M2M5YzRj
""")
st.markdown("""
##### Número de Superanfitriones
""")
col1,col2,col3 = st.columns(3)
with col2:
    listings['host_is_superhost']=listings['host_is_superhost'].replace({"t": "True", "f": "False"})
    feq=listings['host_is_superhost'].value_counts().reset_index()

    fig = px.bar(feq, x='host_is_superhost', y='count', color='host_is_superhost', width=500, height=500,template='plotly_dark',color_discrete_sequence=['#274490','#FF0000'])

    fig.update_layout(
        title="Número de listings con Superanfitrión",
        xaxis_title="Superanfitrión",
        yaxis_title="Número de ofertas",
        )
    st.plotly_chart(fig)


pages=['Toronto', 'East York', 'North York', 'Etobicoke', 'York', 'Scarborough']

selected_page = st.sidebar.selectbox("Rapidez de respuesta por zona", pages)

if selected_page=='Toronto':
    st.markdown("""
##### Rapidez media de respuesta de los anfitriones (zona Toronto, 2 personas alojadas)
""")
    listings1 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='Toronto')&(listings['accommodates']==2)]
    
    tab1,tab2=st.tabs(['Ratio de respuesta','Tiempo de respuesta'])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings1['host_response_rate'].dropna()
            
            fig = px.histogram(feq, x='host_response_rate', width=800, height=400, template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Ratio de respuestas (mínimo 10 reviews)",
                xaxis_title="Porcentaje de respuestas",
                yaxis_title="Número de listings"
            )

            st.plotly_chart(fig)

    with tab2:
        feq=listings1['host_response_time'].value_counts()
        feq=feq.reset_index()
        col1,col2,col3 = st.columns(3)
        with col2:
            fig = px.bar(feq, x='host_response_time', y='count', color='host_response_time', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])
            fig.update_layout(
                title="Rapidez de respuesta (mínimo 10 reviews)",
                xaxis_title="Rapidez de la respuesta",
                yaxis_title="Número de listings",
            )
            st.plotly_chart(fig)

    

elif selected_page=='East York':
    st.markdown("""
##### Rapidez media de respuesta de los anfitriones (zona East York, 2 personas alojadas)
""")
    listings2 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='East York')&(listings['accommodates']==2)]
    tab1,tab2=st.tabs(['Ratio de respuesta','Tiempo de respuesta'])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings2['host_response_rate'].dropna()
            
            fig = px.histogram(feq, x='host_response_rate', width=800, height=400, template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Ratio de respuestas (mínimo 10 reviews)",
                xaxis_title="Porcentaje de respuestas",
                yaxis_title="Número de listings"
            )

            st.plotly_chart(fig)

    with tab2:
        feq=listings2['host_response_time'].value_counts()
        feq=feq.reset_index()
        col1,col2,col3 = st.columns(3)
        with col2:
            fig = px.bar(feq, x='host_response_time', y='count', color='host_response_time', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])

            fig.update_layout(
                title="Rapidez de respuesta (mínimo 10 reviews)",
                xaxis_title="Rapidez de la respuesta",
                yaxis_title="Número de listings",
            )
            st.plotly_chart(fig)

elif selected_page=='North York':
    st.markdown("""
##### Rapidez media de respuesta de los anfitriones (zona North York, 2 personas alojadas)
""")
    listings3 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='North York')&(listings['accommodates']==2)]
    tab1,tab2=st.tabs(['Ratio de respuesta','Tiempo de respuesta'])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings3['host_response_rate'].dropna()
            
            fig = px.histogram(feq, x='host_response_rate', width=800, height=400, template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Ratio de respuestas (mínimo 10 reviews)",
                xaxis_title="Porcentaje de respuestas",
                yaxis_title="Número de listings"
            )

            st.plotly_chart(fig)

    with tab2:
        feq=listings3['host_response_time'].value_counts()
        feq=feq.reset_index()
        col1,col2,col3 = st.columns(3)
        with col2:
            
            fig = px.bar(feq, x='host_response_time', y='count', color='host_response_time', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])

            fig.update_layout(
                title="Rapidez de respuesta (mínimo 10 reviews)",
                xaxis_title="Rapidez de la respuesta",
                yaxis_title="Número de listings",
            )
            st.plotly_chart(fig)

elif selected_page=='Etobicoke':
    st.markdown("""
##### Rapidez media de respuesta de los anfitriones (zona Etobicoke, 2 personas alojadas)
""")
    listings4 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='Etobicoke')&(listings['accommodates']==2)]
    tab1,tab2=st.tabs(['Ratio de respuesta','Tiempo de respuesta'])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings4['host_response_rate'].dropna()
            
            fig = px.histogram(feq, x='host_response_rate', width=800, height=400, template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Ratio de respuestas (mínimo 10 reviews)",
                xaxis_title="Porcentaje de respuestas",
                yaxis_title="Número de listings"
            )

            st.plotly_chart(fig)

    with tab2:
        feq=listings4['host_response_time'].value_counts()
        feq=feq.reset_index()
        st.write(feq1)

        col1,col2,col3 = st.columns(3)
        with col2:

            fig = px.bar(feq, x='host_response_time', y='count', color='host_response_time', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])

            fig.update_layout(
                title="Rapidez de respuesta (mínimo 10 reviews)",
                xaxis_title="Rapidez de la respuesta",
                yaxis_title="Número de listings",
            )
            st.plotly_chart(fig)

elif selected_page=='York':
    st.markdown("""
##### Rapidez media de respuesta de los anfitriones (zona York, 2 personas alojadas)
""")
    listings5 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='York')&(listings['accommodates']==2)]
    tab1,tab2=st.tabs(['Ratio de respuesta','Tiempo de respuesta'])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings5['host_response_rate'].dropna()
            
            fig = px.histogram(feq, x='host_response_rate', width=800, height=400, template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Ratio de respuestas (mínimo 10 reviews)",
                xaxis_title="Porcentaje de respuestas",
                yaxis_title="Número de listings"
            )

            st.plotly_chart(fig)

    with tab2:
        feq=listings5['host_response_time'].value_counts()
        feq=feq.reset_index()
        col1,col2,col3 = st.columns(3)
        with col2:
            

            fig = px.bar(feq, x='host_response_time', y='count', color='host_response_time', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])

            fig.update_layout(
                title="Rapidez de respuesta (mínimo 10 reviews)",
                xaxis_title="Rapidez de la respuesta",
                yaxis_title="Número de listings",
            )
            st.plotly_chart(fig)

elif selected_page=='Scarborough':
    st.markdown("""
##### Rapidez media de respuesta de los anfitriones (zona Scarborough, 2 personas alojadas)
""")
    listings6 = listings[(listings['number_of_reviews']>=10)&(listings['District']=='Scarborough')&(listings['accommodates']==2)]
    tab1,tab2=st.tabs(['Ratio de respuesta','Tiempo de respuesta'])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col2:
            feq=listings6['host_response_rate'].dropna()
            
            fig = px.histogram(feq, x='host_response_rate', width=800, height=400, template='plotly_dark',color_discrete_sequence=['#274490'])

            fig.update_layout(
                title="Ratio de respuestas (mínimo 10 reviews)",
                xaxis_title="Porcentaje de respuestas",
                yaxis_title="Número de listings"
            )

            st.plotly_chart(fig)

    with tab2:
        feq=listings6['host_response_time'].value_counts()
        feq=feq.reset_index()
        col1,col2,col3 = st.columns(3)
        with col2:
            

            fig = px.bar(feq, x='host_response_time', y='count', color='host_response_time', width=800, height=400,template='plotly_dark',color_discrete_sequence=['#59788E','#960018','#3944BC','#D9381E'])

            fig.update_layout(
                title="Rapidez de respuesta (mínimo 10 reviews)",
                xaxis_title="Rapidez de la respuesta",
                yaxis_title="Número de listings",
            )
            st.plotly_chart(fig)

st.markdown("""
    Se puede comprobar que el mayor número de ofertas no pertenecen a un superanfitrión. 
    
    A pesar de esto, se observa en la gráfica de respuestas, que los anfitriones tienen un alto nivel de involucración a la hora de responder a sus clientes, situando la mayoría de ofertas con un índice de respuesta superior al 90% y con un tiempo de respuesta a la hora o a las pocas horas de realizar la consulta.
    """)
#--------------------------------------SUPERANFITRIÓN-------------------------------------#



#--------------------------------------WORD CLOUD-------------------------------------#

st.subheader('Palabras más comunes en las reviews')

col1,col2,col3=st.columns(3)
with col2:
    image1 = Image.open('img/reviews.png')
    st.image(image1)

#--------------------------------------WORD CLOUD-------------------------------------#



#--------------------------------------SIDEBAR-------------------------------------#


image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#