#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from pycaret.regression import *
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Predictor de precios', page_icon='🌆', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

prueba = pd.read_csv("data/prueba.csv")

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#
st.title('Estimador para posibles ofertas')

st.subheader('Detalles de la oferta:')

col1,col2=st.columns(2)
with col1:
    room_type = st.selectbox("Room Type", prueba['room_type'].unique())
    accommodates = st.selectbox("Accommodates", prueba['accommodates'].unique())
    minimum_nights = st.number_input("Minimum Nights", min_value=0, max_value=28)
    availability_365 = st.number_input("Listing Availability (maximum 365 days)", min_value=0, max_value=365)
with col2:
    rental_type = st.selectbox('Rental type',prueba['rental_type'].unique())
    license_disclosed = st.selectbox('License',prueba['license_disclosed'].unique())
    District = st.selectbox('District',prueba['District'].unique())
    filtered_neighbourhoods = prueba[prueba['District'] == District]['neighbourhood'].unique()
    neighbourhood = st.selectbox("Neighbourhood", filtered_neighbourhoods)


def prediccion_precios(room_type, accommodates, minimum_nights, availability_365, District, rental_type, license_disclosed, neighbourhood):
    data = pd.DataFrame({'room_type': [room_type],
                         'accommodates': [accommodates],
                         'minimum_nights': [minimum_nights],
                         'availability_365': [availability_365],
                         'District': [District],
                         'rental_type':[rental_type],
                         'license_disclosed': [license_disclosed],
                         'neighbourhood': [neighbourhood]})
    
    loaded_model = load_model('price_prediction_regression')
    prediction = predict_model(loaded_model, data=data)
    
    return np.round(prediction.loc[0,'prediction_label'],2)

precio = prediccion_precios(room_type, accommodates, minimum_nights, availability_365, District, rental_type, license_disclosed, neighbourhood)

if st.button('Precio 👈'):
    st.write('El precio diario estimado para la oferta es', precio, 'CAD')
    st.write('En una estancia mínima de', minimum_nights, 'noches, el total es', np.round((precio*minimum_nights),2), 'CAD')
else:
    st.write('📝 Estimando ... ')



#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#