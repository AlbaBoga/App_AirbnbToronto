#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd



import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import streamlit as st
from PIL import Image


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

    link = '<iframe title="Report Section" width="1024" height="1060" src="https://app.powerbi.com/view?r=eyJrIjoiMzBmMTAxZmMtZWVlMC00NGQ2LWFkYjYtZTAwOTkzZTFkYTRkIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>'

    st.markdown(link, unsafe_allow_html=True)



#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#