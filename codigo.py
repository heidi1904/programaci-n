#$ pip instalar streamlit --actualizar
importar  streamlit  como  st
importar  pandas  como  pd
importar  numpy  como  np 
importar  urllib . solicitud
desde  streamlit_option_menu  importar  option_menu
importar  matplotlib . pyplot  como  plt
importar  plotly . expresar  como  px
importar  plotly . figure_factory  como  ff
importar  gdown
de  imagen de importación PIL  

#------------------------------------------------- ------------------
st . set_page_config ( diseño = 'ancho' , initial_sidebar_state = 'expandido' )
con  abierto ( 'logo.css' ) como  f :
    st . markdown ( f'<estilo> { f . leer () } </logo>' , unsafe_allow_html = True )
con  st . barra lateral :  
    st . descuento ( '###' )
    st . barra lateral header ( 'Catálogo Sísmico: 1960-2021' )
    st . barra lateral info ( 'Visualización y exploración de la base de datos sísmicos elaborados por el Instituto Geofísico del Perú (IGP).' )
    seleccionado  =  menú_opción (
        menu_title  =  'Menú' ,
        opciones  = [ 'Inicio' , 'Mapas' , 'Equipo' ],
        iconos  = [ 'casa' , 'mapa' , 'personas' ],
        menu_icon = 'transmitir' ,
        índice_predeterminado  =  0 ,
        estilos  = {
            "nav-link-selected" :{ "background-color" : "purple" }
        },
    )
#---------------------------INICIO------------------------------------- ------------
si se  selecciona  ==  'Inicio' :
    st . markdown ( "<h1 style ='text-align: center'>Sismos ocurridos en el Perú para el período: 1960-2021</h1>" , unsafe_allow_html = True )
    st . descuento ( '____' )
    st . subtítulo ( 'Contexto:' )
    st . write ( "A nivel mundial, el Perú es uno de los países de mayor potencial sísmico debido a que forma parte del denominado Cinturón de Fuego del Pacífico, como consecuencia de los procesos de convección del manto del planeta. En este sentido, la actividad sísmica en torno a ella genera diferentes procesos de convergencia entre las placas tectónicas. En Sudamérica, las placas Nazca y Sudamericana convergen, desarrollando una geodinámica activa y, por ende, una actividad sísmica frecuente." )
    st . descuento ( '###' )
    st . write ( '**Figura 1.** Cinturón de Fuego del Pacífico' )
    imagen  =  Imagen . abierto ( 'cinturondefuego.png' )
    st . imagen ( imagen )
    st . caption ( 'El cinturón de fuego del Pacífico o anillo de fuego, es una región de 40.000 kilómetros de largo, distribuidos en tres continentes. Se caracteriza por concentrar algunas de las zonas de subducción más importantes del mundo, lo que ocasiona una intensa actividad sísmica y volcánica.' )
    st . descuento ( '###' )
    st . subtítulo ( 'INSTITUTO GEOFÍSICO DEL PERÚ (IGP)' )
    st . write ( 'El IGP es la entidad encargada de investigar y monitorear los procesos geofísicos en territorio peruano. Si bien el IGP ha logrado determinar las ubicaciones y posibles magnitudes de futuros sismos, aún no es posible la determinación del día y la hora.' )
    imagen  =  Imagen . abierto ( 'IGP.png' )
    st . imagen ( imagen )
    st.subheader('Dataset: Catalogo Sísmico 1960-2021')
    st.write("Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este dataset se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021 con datos proporcionados por el Instituto Geofísico del Perú (IGP).")
    st.caption('Fecha de última actualización: 31/12/2021, 20:00 (UTC-05:00)')
    @st.experimental_memo
    def download_data():
	@@ -58,21 +58,28 @@ def download_data():
    st.caption('Fuente del dataset: https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp')
    st.markdown('###')

    st.subheader("Histogramas de datos sísmicos entre 1960-2021")
    st.write('Dependiendo de la profundidad del hipocentro de energía liberada en un terremoto, es que podemos clasificarlos en tres tipos: superficiales, intermedios y profundos.')
    st.write('El hipocentro o foco es el punto donde se libera la energía en un terremoto. Por su parte, el epicentro es el lugar de la superficie terrestre que se ubica exactamente sobre el hipocentro del terremoto. El tipo de magnitud se registra de acuerdo a la profundidad característica que tuvo lugar el sismo. Para esto, podemos clasificar en tres tipos los terremotos:')
    st.write('**Profundidad superficial:** Su foco se encuentra entre los 70 km de profundidad, comúnmente son los más destructivos porque impacta directamente con la superficie y en lo general su hipocentro se encuentra entre los 10 y 25 km de profundidad.')
    st.write('**Profundidad intermedia:** Con profundidades entre los 70 y 300 km.')
     st.write('**Profundidad profunda:** El foco se halla a más de 300 km de profundidad, sobrepasan la litósfera, casi no se sienten por lo lejos que se encuentran de la superficie y también son poco frecuentes.')
    st.write('**Según profundidad:**')
    for i in range(5,6):
        fig = px.histogram(df_catalogo, df_catalogo.columns[i])
        st.plotly_chart(fig, use_container_width=True)
    st.caption('**Figura 1:** Histograma de frecuencia de sismos en función de la profundidad de los focos sísmicos.')    
    st.write('**Según magnitud:**')
    st.markdown("###")
    bar_chart = df_catalogo.MAGNITUD.value_counts()
    bar_chart = pd.DataFrame(bar_chart)
    bar_chart.columns = ['Magnitud del sismo']
    st.bar_chart(bar_chart)
    st.caption('**Figura 2:** Histograma de frecuencia de sismos en función del rango de magnitud.')  

#---------------------------MAPAS-------------------------------
df_local=pd.read_excel("Catalogo.xlsx")
df_intermedia = pd.read_csv("https://raw.githubusercontent.com/heidi1904/programaci-n/main/intermedia.xlsx%20-%20catalogo.csv")

if selected == 'Mapas':
    st.markdown("<h1 style ='text-align: center'>Mapa sísmico del Perú</h1>", unsafe_allow_html=True)
	@@ -89,6 +96,22 @@ def download_data():
    st.image(image)
    st.write("**Fuente:** Instituto Geofísico del Perú")
    st.markdown('____')
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


    dataset = st.selectbox(
        'Seleccione una opción:',
        ('Profundidad superficial',
	@@ -100,14 +123,6 @@ def download_data():
        option = 'profundidad superficial'
        st.markdown("###")
        st.subheader('**Sismos registrados con '+option+' durante 1960-2021.**')


    elif dataset == 'Profundidad intermedia':
	@@ -126,40 +141,27 @@ def intermedia_data():
        st.map(data)
        st.markdown("###")
        st.dataframe(df_intermedia)
        cant = len(df_intermedia.axes[0]) 
            

    elif dataset == 'Profundidad profunda':
        option = 'profundidad profunda'
        st.markdown("###")
        st.subheader('**Sismos registrados con '+option+' durante 1960-2021.**')


     
    st.write('Se encontraron', cant,'registros de sismos para su búsqueda.') 
    st.map(data_map)





#-----------------------------EQUIPO----------------------------    
if selected == 'Equipo':
    st.markdown("<h1 style ='text-align: center'>¿Quiénes somos?</h1>", unsafe_allow_html=True)
    st.markdown('____')
    st.write("Somos un grupo de estudiantes del 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia (UPCH), buscamos que el usuario que ingrese a nuestra página pueda revisar de forma sencilla la magnitud que registraron los sismos entre los años 1960 y 2021 mediante un dashboard.")
    image = Image.open('Foto grupal.jpg')
    st.image(image)
