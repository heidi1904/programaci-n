#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
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
