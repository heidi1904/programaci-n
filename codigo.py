#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('upch.css') as f:
    st.markdown(f'<style>{f.read()}</upch>', unsafe_allow_html=True)
with st.sidebar: 
    st.markdown("###")
    st.sidebar.header('Programación Avanzada')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Reporte','Equipo'],
        icons = ['house', 'book', 'people'],
        menu_icon='cast',
        default_index = 0,
        styles ={
            "nav-link-selected":{"background-color":"purple"}
        },
    )
#---
if selected == 'Inicio':
    st.markdown("<h1 style ='text-align: center'>Sismos ocurridos en el Perú para el período: 1960-2021</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021.")
    st.header("Dataset")
    
    @st.experimental_memo
    def download_data():
        url ="https://raw.githubusercontent.com/heidi1904/programaci-n/main/Catalogo.xlsx%20-%20Catalogo1960_2021.csv"
        filename ="Catalogo.xlsx%20-%20Catalogo1960_2021.csv"
        urllib.request.urlretrieve(url,filename)
        
        
    download_data()
    df_cat = pd.read_csv('Catalogo.xlsx%20-%20Catalogo1960_2021.csv') 
    st.dataframe(df_cat)
   
    st. header("Sismos ocurridos en el Perú para el período 1960-2021")
    st.write("Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021.")
    st . header ( "Histogramas de datos sísmicos:" )
    for i in range(5,7):
        group_labels = ['y', 'x']
        fig = px.histogram(df_cat, df_cat.columns[i])
        st.plotly_chart(fig, use_container_width=True)
    
if selected == 'Reporte':
    st.markdown("<h1 style ='text-align: center'>Lugares afectados</h1>", unsafe_allow_html=True)
    @st.cache
    def localizacion_data():
        df_local = pd.read_csv('Catalogo.xlsx%20-%20Catalogo1960_2021.csv')
        df_local = df_local.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
        return df_local
    data = localizacion_data()
    st.map(data)        
        
        
        
        
    
if selected == 'Equipo':
    st.markdown("____________________________________________________________________")
    st.markdown("<h1 style ='text-align: center'>Equipo</h1>", unsafe_allow_html=True)
    image = Image.open('MP.jpg')
    st.image(image)
    st.write("escribir normal")
    st.subheader("escribir subtitulo")
    st.write("**escribir en negrita**")
    st.caption('info en gris')
    st.markdown("--- linea")
    st.markdown("### espaacio") 

    
    

    
    
