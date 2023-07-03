#--------------LIBRERÍAS--------------#
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Predictor de precios', page_icon='🌆', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

st.title('Estimador para posibles ofertas')

if st.button('Redirección 👈'):
    pass
else:
    st.write('📝 Estimando ... ')

#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/flagToronto.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#