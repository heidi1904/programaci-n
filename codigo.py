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
with open('logo.css') as f:
    st.markdown(f'<style>{f.read()}</logo>', unsafe_allow_html=True)
with st.sidebar:  
    st.markdown('###')
    st.sidebar.header('Catálogo Sísmico: 1960-2021')
    st.sidebar.info('Visualización y exploración de la base de datos sísmicos elaborado por el Instituto Geofísico del Perú (IGP).')
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
    st.markdown('____')
    st.subheader('Contexto:') 
    st.write("A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado Cinturón de Fuego del Pacífico, como consecuencia de los procesos de convección del manto del planeta. En este sentido, la actividad sísmica en torno a ella genera diferentes procesos de convergencia entre las placas tectónicas. En Sudamérica, las placas Nazca y Sudamericana convergen, desarrollando una geodinámica activa y, por ende, una actividad sísmica frecuente.")
    st.markdown('###')
    st.write('**Figura 1.** Cinturón de Fuego del Pacífico')
    image = Image.open('cinturondefuego.png')
    st.image(image)
    st.caption('El cinturón de fuego del Pacífico o anillo de fuego, es una región de 40.000 kilómetros de largo, distribuidos en tres continentes. Se caracteriza por concentrar algunas de las zonas de subducción más importantes del mundo, lo que ocasiona una intensa actividad sísmica y volcánica.')
    st.markdown('###')
    
    st.subheader('Dataset: Catalogo Sísmico 1960-2021')
    st.write("A continuación, se presenta la base de datos sísmicos que contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud.")
    st.caption('Fecha de última actualización: 31/12/2021, 20:00 (UTC-05:00)')
    @st.experimental_memo
    def download_data():
        url = "https://drive.google.com/uc?id=1XKCOchqhncJV6rm_osfHqqb7sVXX0FI4"
        ouput = "Catalogo.xlsx"
        gdown.download(url,ouput,quiet = False)
    download_data()
    df_catalogo = pd.read_excel('Catalogo.xlsx') 
    st.dataframe(df_catalogo)
    st.caption('Fuente del dataset: https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp')
    st.markdown('###')
    
    st.subheader("Histogramas de datos sísmicos:")
    for i in range(5,7):
        fig = px.histogram(df_catalogo, df_catalogo.columns[i])
        st.plotly_chart(fig, use_container_width=True)
        
    st.subheader("Sismos registrados según magnitud entre 1960-2021.")
    st.markdown("###")

    bar_chart = df_catalogo.MAGNITUD.value_counts()
    bar_chart = pd.DataFrame(bar_chart)
    bar_chart.columns = ['Magnitud del sismo']
    st.bar_chart(bar_chart)
    
#-------------------------------------------------------------------

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
    
    

#-------------------------------------------------------------------    
if selected == 'Equipo':
    st.markdown("<h1 style ='text-align: center'>¿Quiénes somos?</h1>", unsafe_allow_html=True)
    st.markdown('____')
    st.write("Somos un grupo de estudiantes del 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia (UPCH), buscamos que el usuario que ingrese a nuestra página pueda revisar de forma sencilla la magnitud que registraron los sismos entre los años 1960 y 2021 mediante un dashboard.")
    image = Image.open('Foto grupal.jpg')
    st.image(image)
