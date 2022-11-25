#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from streamlit_option_menu import option_menu
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
#import plotly.figure_factory as ff
#import scipy


with st.sidebar: 
    st.markdown("###")
    st.sidebar.header('Programación Avanzada')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Reporte','Equipo'],
        icons = ['house', 'book', 'book','people'],
        menu_icon='cast',
        default_index = 0,
    )

if selected == 'Inicio':
    st.markdown("<h1 style ='text-align: center'>"Sismos ocurridos en el Perú para el período 1960-2021":</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021.")
    st.header("Dataset")
  
  @st.experimental_memo
  def download_data():
        url ="https://raw.githubusercontent.com/heidi1904/programaci-n/main/Catalogo.xlsx%20-%20Catalogo1960_2021.csv"
        filename ="Catalogo.xlsx%20-%20Catalogo1960_2021.csv"
        urllib.request.urlretrieve(url,filename)
        df = pd.read_csv('Catalogo.xlsx%20-%20Catalogo1960_2021.csv')
        return df
  download_data()
  st.dataframe(download_data())
    
if selected == 'Reporte':
        st.markdown("<h1 style ='text-align: center'>Titulo:</h1>", unsafe_allow_html=True)
        
        st.header("Histogramas de datos sísmicos:")
        for i in range(5,7):
            fig = px.histogram(df_cat, df_cat.columns[i])
            st.plotly_chart(fig, use_container_width=True)
    
    
   # option = st.selectbox('¿Si desea más información puede contactarnos mediante las siguientes opciones?',('Email', 'Teléfono', 'Whatsapp', 'Instagram'))
   # st.write('Seleccionó:', option)

    

  
  
