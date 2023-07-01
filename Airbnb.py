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
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Toronto Airbnb', page_icon='🐻', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#


#--------------------------------------TÍTULO-------------------------------------#
image2 = Image.open('img/toronto.jpg')
st.image(image2, width=800)

st.title('Análisis de las ofertas de Airbnb en Toronto')

st.subheader('¿Por qué visitar Toronto?')
st.markdown(
            """
Canadá no es sólo un lugar mágico, con paisajes únicos, que te dejarán sin aliento en cualquier estación del año. Sus ciudades, en concreto, Toronto, tienen mucho más que ofrecer, a parte de fauna y flora. Una ciudad donde reina la variedad arquitectónica, el ocio, la cultura y el entretenimiento deportivo. 

Entre los diferentes encantos de la ciudad, cabe destacar:
* Barrios como Rosedale, Forest Hill o Cabbagetown, rodeados de edificios de estilo victoriano o eduardiano, rompiendo con la monotonía que ofrecen los rascacielos dentro del distrito financiero.
* Arquitectura gótica y Art Déco, que destaca sobre la arquitectura contemporánea que poseen los edificios más nuevos de Toronto, como puede ser el ayuntamiento de Toronto, construido sobre los moldes de la arquitectura Romanesque Revival, que data de 1896 o la Casa Loma, una mansión reconvertida a atracción turística, completada en 1914, que imita el castillo de Balmoral de Escocia.
* Para aquellos con intereses culturales, Toronto posee el Real Museo de Ontario, el museo más grande de Canadá, con una de las colecciones más detalladas de la Antigua China y la Compañía de Ópera de Canadá, la más importante del país y la sexta más importante en Norteamérica.
* Además de sus parques y playas, en Toronto puedes encontrar el Lago de Ontario, una atracción turística muy conocida, ya que se congela durante los fríos días de invierno.
* A pocos kilómetros se puede disfrutar de las Cataratas del Niágara, que además del paisaje, suponen la frontera con Estados Unidos.
* Para los apasionados por el deporte, Toronto es la única ciudad canadiense con casi todas las ligas deportivas, pudiendo disfrutar de fútbol, hockey, béisbol, rugby, entre otras.
* Para aquellos que disfruten de las ciudades más cosmopolitas, en Toronto se encuentra la Torre CN, la torre de radiodifusión más alta de América.
* Finalmente, por su comida y gran diversidad cultural, gracias a que Toronto conserva barrios con diversas identidades étnicas, como el barrio griego, el barrio chino o Little Italy.

Info:
https://es.wikipedia.org/wiki/Toronto

https://mikeandlauratravel.com/is-toronto-worth-visiting/#:~:text=From%20world%2Dclass%20museums%20and,never%20be%20bored%20in%20Toronto.
        """
        )

st.subheader('El papel de Airbnb en Toronto')
st.markdown(
            """
Los denominados alquileres a corto plazo han supuesto un gran impacto en ciudades con gran potencial turístico. A pesar de la gran variedad de hoteles que Toronto puede ofrecer, no hay nada como ser capaces de disfrutar del paisaje de una ciudad en tu día a día, sintiéndote parte de ella. Airbnb ofrece esta posibilidad, permitiendo a los turistas vivir en los diferentes barrios y zonas de Toronto de una forma inmersiva, ofreciendo una experiencia turística que va más allá de lo convencional.

Además, no sólo supone una experiencia añadida a tus viajes, sino que también es un ahorro con respecto a lo que podrías gastar durante tu estancia en un hotel. Esto les permite a los turistas invertir su dinero en la cultura y el ocio de la ciudad, haciendo sus estancias no sólo más placenteras, sino también más largas.

Mientras que el precio de la propiedad continúa subiendo en diferentes zonas de Toronto, gracias al gran volumen de turistas que está experimentando, una encuesta realizada en 2016 a los clientes de Airbnb afirma que el 2.3% de los mismos no hubiese visitado la ciudad si el servicio no estuviese disponible, mientras que el 32% de ellos afirma que no hubiesen extendido tanto su visita por no ser de Airbnb. Esto supondría unas pérdidas para la ciudad de 40 millones de dólares canadienses, en base a las estimaciones de gasto por turista.

Por estas razones, Airbnb ha sido clave en el crecimiento de la ciudad, permitiendo no sólo su expansión turística, sino también la creación de nuevos empleos y la mejora de todas aquellas posibilidades de ocio y cultura que tiene para ofrecer.

Info: https://www.airbnbcitizen.com/wp-content/uploads/2017/02/airbnb-Economic-Impact-Statement-Toronto-Final-released.pdf
        """
        )
#--------------------------------------TÍTULO-------------------------------------#



#--------------------------------------SIDEBAR-------------------------------------#


image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#