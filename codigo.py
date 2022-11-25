#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from streamlit_option_menu import option_menu

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
  st.markdown("<h1 style ='text-align: center'>Titulo:</h1>", unsafe_allow_html=True)
  st.markdown("---")
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
  
  
