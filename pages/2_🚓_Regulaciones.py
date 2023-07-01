#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



#to make the plotly graphs
import plotly.graph_objs as go
import plotly.express as px

import streamlit as st
from PIL import Image

#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Regulaciones por el gobierno de Toronto', page_icon='🌆', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

listings = pd.read_csv("data/listings_final.csv")

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#



#--------------------------------------TÍTULO-------------------------------------#
st.title('Regulaciones por el gobierno de Toronto')
st.subheader('Análisis de las ofertas en función de las regulaciones')
st.markdown(
            """
El gobierno de Toronto ha establecido una serie de reglas para regular los alquileres dentro de la plataforma Airbnb. Estas normas son de gran interés en el análisis de los datos para comprobar potenciales incumplimientos de las mismas.

Las normas principales a tener en cuenta:
* Se considera que las ofertas de alquiler en empresas como Airbnb, son considerados alquileres de corta duración, por lo que se estima que no se puede realizar el alquiler de las propiedades por más de 28 días consecutivos.
* Todos aquellos anfitriones que realicen alquileres de corta duración deben de estar registrados en la ciudad de Toronto y deben proporcionar su número de licencia.
* El alquiler se realiza de la residencia primaria o principal.
* Los anfitriones deben residir en la zona.
* Si el alquiler va destinado a una residencia completa, no puede superar el total de 180 noches por año.
* Si el alquiler va destinado a una habitación dentro de la residencia, no habría límite de noches, pero lo anfitriones no pueden alquilar más de tres habitaciones dentro de su residencia.

Info: https://www.toronto.ca/community-people/housing-shelter/short-term-rentals/short-term-rental-operators-hosts/?accordion=comply-with-the-regulations

https://www.toronto.ca/community-people/housing-shelter/short-term-rentals/

https://airbtics.com/airbnb-regulations-in-toronto/
        """
        )

#--------------------------------------TÍTULO-------------------------------------#



#--------------------------------------ALQUILER A CORTO PLAZO-------------------------------------#

st.subheader('Tipo de alquiler')

listings['rental_type']=None
listings.loc[listings['minimum_nights']>28,'rental_type']='Long-term rental'
listings.loc[listings['rental_type'].isnull(),'rental_type']='Short-term rental'

tab1,tab2,tab3=st.tabs(['Proporción de tipo de alquiler','Distribución de tipo de alquiler','Distribución por zonas'])

with tab1:
    col1,col2,col3 = st.columns(3)
    with col2:
        feq=listings['rental_type'].value_counts()
        fig=px.pie(feq ,names = feq.index, values=feq.values,width = 1000, template= "plotly_dark", title="Tipo de oferta",color_discrete_sequence=['#274490','#FF0000'])
        st.plotly_chart(fig)
with tab2:
    col1,col2,col3 = st.columns(3)
    with col2:
        not_regulated = listings[listings['rental_type']=='Long-term rental']
        not_regulated = not_regulated[['name','host_id', 'host_name', 'latitude', 'longitude']]
        not_regulated.index.name ='listing_id'
        fig=px.scatter_mapbox(not_regulated, lat='latitude', lon='longitude', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas de alquiler a largo plazo', template= "plotly_dark", size_max=80,hover_name='name',color_discrete_sequence=['#274490'])
        st.plotly_chart(fig)
with tab3:
    col1,col2,col3 = st.columns(3)
    with col2:
        rental=listings.groupby('District')['rental_type'].value_counts().reset_index()
        fig=px.bar(rental,x='District',y='count', color='rental_type', title= "Ofertas y tipo de alquiler",template= "plotly_dark", width = 1000,color_discrete_sequence=['#274490','#FF0000'])
        fig.update_layout(
            yaxis_title="Número de ofertas",
            xaxis_title="Área"
        )
        st.plotly_chart(fig)

st.markdown(
            """
Se observa que más de un 15% de las ofertas ofrecen más de 28 noches como número máximo de noches, lo cual dejaría de ser considerado alquiler de corta duración.

Comprobando la distribución de estos alquileres por la zona, se puede comprobar que en la zona de Toronto es donde está el mayor número de ofertas, que es donde se concentra la mayor actividad turística.
        """
        )

#--------------------------------------ALQUILER A CORTO PLAZO-------------------------------------#



#--------------------------------------LICENCIAS-------------------------------------#

st.subheader('Licencias')

listings['license_disclosed']=None
listings.loc[listings['license'].isnull(),'license_disclosed']='No'
listings.loc[listings['license']=='Exempt','license_disclosed']='Exempt'
listings.loc[listings['license_disclosed'].isnull(),'license_disclosed']='Yes'

tab1,tab2,tab3=st.tabs(['Proporción de ofertas con y sin licencia','Distribución de ofertas sin licencia','Distribución por zonas'])

with tab1:
    col1,col2,col3 = st.columns(3)
    with col2:
        feq=listings['license_disclosed'].value_counts()
        fig=px.pie(feq ,names = feq.index, values=feq.values,width = 1000, template= "plotly_dark", title="Ofertas con y sin licencia mostrada",color_discrete_sequence=['#274490','#FF0000','#52B2BF'])
        st.plotly_chart(fig)
with tab2:
    col1,col2,col3 = st.columns(3)
    with col2:
        not_regulated1 = listings[listings['license_disclosed']=='No']
        not_regulated1 = not_regulated1[['name','host_id', 'host_name', 'latitude', 'longitude']]
        not_regulated1.index.name ='listing_id'
        fig=px.scatter_mapbox(not_regulated1, lat='latitude', lon='longitude', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas sin licencia', template= "plotly_dark", size_max=80,hover_name='name',color_discrete_sequence=['#274490'])
        st.plotly_chart(fig)
with tab3:
    col1,col2,col3 = st.columns(3)
    with col2:
        license=listings.groupby('District')['license_disclosed'].value_counts().reset_index()
        fig=px.bar(license,x='District',y='count', color='license_disclosed', title= "Ofertas con y sin licencia mostrada",template= "plotly_dark", width = 1000,color_discrete_sequence=['#274490','#FF0000','#52B2BF'])
        fig.update_layout(
            yaxis_title="Número de ofertas",
            xaxis_title="Área"
        )
        st.plotly_chart(fig)

st.markdown(
            """
Más del 50% de las ofertas listadas no especifican su número de licencia, siendo esencial en la ciudad de Toronto para tener permitido el alquiler a corto plazo. Se han encontrado más de 10000 ofertas diferentes que no especifican la licencia, de las cuales más del 70% se concentran en la zona de Toronto.
        """
        )

#--------------------------------------LICENCIAS-------------------------------------#



#--------------------------------------NÚMERO MÁXIMO DE NOCHES-------------------------------------#

st.subheader('Máximo número de noches para estancias en casas o apartamentos')

col1,col2,col3 = st.columns(3)
with col2:
    not_regulated2=listings[listings['room_type']=='Entire home/apt'].groupby(['id','host_id','maximum_nights'])['room_type'].value_counts().reset_index()
    not_regulated2=not_regulated2[not_regulated2['maximum_nights']>180]
    listado2 = listings[listings['id'].isin(not_regulated2['id'])][['name', 'host_id', 'host_name', 'latitude', 'longitude']]
    st.write('Número de ofertas con un máximo número de noches que supera 180 días al año:')
    st.write(listado2.shape[0])
    fig=px.scatter_mapbox(listado2, lat='latitude', lon='longitude', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas que superan el número máximo de noches', template= "plotly_dark", size_max=80,hover_name='name',color_discrete_sequence=['#274490'])
    st.plotly_chart(fig)

st.markdown(
            """
Se han encontrado un total de 8575 ofertas que alquilan apartamentos o casas que no cumplen con la limitación de 180 noches como máximo por año.
"""
        )

#--------------------------------------NÚMERO MÁXIMO DE NOCHES-------------------------------------#



#--------------------------------------ALQUILER DE PROPIEDAD PRINCIPAL-------------------------------------#

st.subheader('Alquiler de propiedad principal')

col1,col2,col3 = st.columns(3)
with col2:
    not_regulated4=listings[listings['room_type']=='Entire home/apt'].groupby('host_id')['room_type'].value_counts().reset_index()
    not_regulated4=not_regulated4[not_regulated4['count']>1]
    st.write('Número de anfitriones con más de una propiedad alquilada:')
    st.write(not_regulated4.shape[0])
    listado1 = listings[listings['host_id'].isin(not_regulated4['host_id'])][['name', 'host_id', 'host_name', 'latitude', 'longitude','room_type']]
    listado1=listado1[listado1['room_type']=='Entire home/apt']
    fig=px.scatter_mapbox(listado1, lat='latitude', lon='longitude', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas que alquilan más de una propiedad', template= "plotly_dark", size_max=80,hover_name='name',color_discrete_sequence=['#274490'])

    st.plotly_chart(fig)

st.markdown(
            """
En el caso del alquiler de propiedades principales, se han descubierto 1141 anfitriones que tienen más de una propiedad listada para alquiler.
"""
        )

#--------------------------------------ALQUILER DE PROPIEDAD PRINCIPAL-------------------------------------#



#--------------------------------------ALQUILER DE HABITACIONES-------------------------------------#

st.subheader('Número máximo de habitaciones alquiladas')

col1,col2,col3 = st.columns(3)
with col2:
    not_regulated3=listings[(listings['room_type']=='Private room')|(listings['room_type']=='Shared room')].groupby('host_id')['room_type'].value_counts().reset_index()
    not_regulated3=not_regulated3[not_regulated3['count']>3]
    st.write('Número de anfitriones con más de tres habitaciones para alquilar:')
    st.write(not_regulated3.shape[0])
    listado1 = listings[listings['host_id'].isin(not_regulated3['host_id'])][['name', 'host_id', 'host_name', 'latitude', 'longitude','room_type']]
    listado1=listado1[(listado1['room_type']=='Private room')|(listado1['room_type']=='Shared room')]
    fig=px.scatter_mapbox(listado1, lat='latitude', lon='longitude', zoom=10, mapbox_style='carto-positron', title='Distribución de ofertas que superan el número máximo de habitaciones', template= "plotly_dark", size_max=80,hover_name='name',color_discrete_sequence=['#274490'])

    st.plotly_chart(fig)

st.markdown(
            """
Para este último caso, se han encontrado más de 260 anfitriones que ofrecen más de tres habitaciones privadas o compartidas para alquilar.
"""
        )

#--------------------------------------ALQUILER DE HABITACIONES-------------------------------------#



#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#