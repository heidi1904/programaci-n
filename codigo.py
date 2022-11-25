#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import streamlit_option_menu import option_menu

with st.sidebar:
  selected=option_menu(
    mentu_title='Menu',
    options =['Inicio', 'Reporte','Equipo'],
    icons=['house', 'book', 'people'],
    menu_icon='cast',
    default_idex=0,
  )
  
