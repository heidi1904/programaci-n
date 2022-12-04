#$ pip install streamlit --upgrade 
import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import gdown
from PIL import Image

#-------------------------------------------------------------------
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('upch.css') as f:
    st.markdown(f'<style>{f.read()}</upch>', unsafe_allow_html=True)
    st.markdown('####')
    st.sidebar.header('Catálogo Sísmico')
with st.sidebar: 
    st.markdown('####')
    selected = option_menu(
        menu_title = 'Menú',
        options = ['Inicio', 'Mapas','Equipo'],
        icons = ['house', 'map', 'people'],
        menu_icon='cast',
        default_index = 0,
        styles ={
            "nav-link-selected":{"background-color":"purple"}
        },
    )
#-------------------------------------------------------------------
if selected == 'Inicio':
    st.markdown("<h1 style ='text-align: center'>Sismos ocurridos en el Perú para el período: 1960-2021</h1>", unsafe_allow_html=True)
    st.markdown('----')
    st.write("A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado Cinturón de Fuego del Pacífico, debido a los procesos de convección del manto del planeta. En este sentido, la actividad sísmica en torno a ella genera diferentes procesos de convergencia entre las placas tectónicas. En Sudamérica, las placas Nazca y Sudamericana convergen, desarrollando una geodinámica activa y, por ende, una actividad sísmica frecuente. Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021.")
    st.header("Dataset")
    
    @st.experimental_memo
    def download_data():
        url ="https://drive.google.com/uc?id=1XKCOchqhncJV6rm_osfHqqb7sVXX0FI4"
        ouput ="Catalogo.xlsx"
        gdown.download(url,ouput,quiet = False)
        
    download_data()
    df_cat = pd.read_excel('Catalogo.xlsx') 
    st.dataframe(df_cat)
    st . header ( "Sismos ocurridos en el Perú para el período 1960-2021" )
    st.write("Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021.")
    st.subheader("Histogramas de datos sísmicos:")
    for i in range(5,7):
        group_labels = ['y', 'x']
        fig = px.histogram(df_cat, df_cat.columns[i])
        st.plotly_chart(fig, use_container_width=True)

#-----
df_local=pd.read_excel("Catalogo.xlsx")
if selected == 'Mapas':
    st.markdown("<h1 style ='text-align: center'>Mapa sísmico del Perú</h1>", unsafe_allow_html=True)
    st.markdown("____________________________________________________________________")
    st.write("Un mapa sísmico representa la distribución espacial de los eventos sísmicos que dieron lugar en el Perú. La información obtenida fue a partir de la Plataforma Nacional de Datos Abiertos extraídos del Instituto Geofísico del Perú (IGP). Los sismos fueron clasificados según su profundidad: Superficiales, Intermedios y Profundos.")
    image = Image.open('Mapa_sismico.jpg')
    st.image(image)
    st.write("**Fuente:** MINAM ")
    st.markdown("____________________________________________________________________")
    st.write('''El Dr. Hernando Tavera, investigador científico en sismología y geofísica, también director de la Subdirección de Ciencias de la Tierra Sólida (SCTS) del Instituto Geofísico del Perú (IGP); destaca que esta información es de vital importancia para que las municipalidades tomen las medidas de prevención necesarias para reducir el Riesgo de Desastres Naturales ante peligros inminentes como los sismos e inundaciones. 
“El mapa muestra la distribución espacial de todos los sismos ocurridos desde el año 1960… con magnitudes mayores y/o iguales a 4.0 Mw. Estos eventos fueron clasificados en función de la profundidad a la cual ocurren en superficiales, intermedios y profundos, remarcando que en nuestro país los sismos están presentes hasta profundidades del orden de 700 km”, señaló.
''')
    image = Image.open('Image_Dr.jpg')
    st.image(image)
    st.write("**Fuente:** Instituto Geofísico del Perú")
    #df_local=pd.read_csv("https://raw.githubusercontent.com/heidi1904/programaci-n/main/Catalogo.xlsx%20-%20Catalogo1960_2021.csv")
    @st.cache
    def localizacion_data():
        df_local = pd.read_excel('Catalogo.xlsx')
        df_local = df_local.rename(columns={
                'LATITUD':'lat',
                'LONGITUD':'lon',
            })
        return df_local
    data = localizacion_data()
    data1=data[data["PROFUNDIDAD"]<=60]
    #data2=data[data["PROFUNDIDAD"]<=300]
    data_map=data1[["lat","lon"]]
    st.map(data_map)        

#---    
if selected == 'Equipo':
    st.markdown("<h1 style ='text-align: center'>Equipo</h1>", unsafe_allow_html=True)
    st.markdown("____________________________________________________________________")
    st.subheader("¿Quiénes somos?")
    image = Image.open('Foto grupal.jpg')
    st.image(image)
    st.write("Somos un grupo de estudiantes del 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia (UPCH), buscamos que el usuario que ingrese a nuestra página pueda revisar de forma sencilla la magnitud que registraron los sismos entre los años 1960 y 2021 mediante un dashboard.")
    st.subheader("escribir subtitulo")
    st.write("**escribir en negrita**")
    st.caption('info en gris')
    st.markdown("--- linea")
    st.markdown("### espaacio") 

    
    

    
    
