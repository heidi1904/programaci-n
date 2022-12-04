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
    st . subheader ( 'Conjunto de datos: Catálogo Sísmico 1960-2021' )
    st . write ( "Esta base de datos sísmicos contiene todos los parámetros que caracterizan a un sismo, calculados en las mismas condiciones a fin de constituirse como una base homogénea: fecha, hora, latitud, longitud, profundidad y magnitud. En este conjunto de datos se podrá encontrar el Catálogo de Sismos Instrumentales para el período de 1960 – 2021 con datos proporcionados por el Instituto Geofísico del Perú (IGP)." )
    st . caption ( 'Fecha de última actualización: 31/12/2021, 20:00 (UTC-05:00)' )
    @ calle . nota_experimental
    def  descargar_datos ():
        URL  =  "https://drive.google.com/uc?id=1XKCOchqhncJV6rm_osfHqqb7sVXX0FI4"
        salida  =  "Catálogo.xlsx"
        gbajar _ descargar ( url , salida , silencioso  =  Falso )
    descargar_datos ()
    df_catalogo  =  pd . read_excel ( 'Catálogo.xlsx' )
    st . marco de datos ( df_catalogo )
    st . caption ( 'Fuente del dataset: https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp' )
    st . descuento ( '###' )
    
    st . subheader ( "Histogramas de sismo entre 1960-2021." )
    st . write ( '**Según profundidad:**' )
    para  i  en  rango ( 5 , 6 ):
        higo  =  px . histograma ( df_catalogo , df_catalogo . columnas [ i ])
        st . plotly_chart ( fig , use_container_width = True )
    st . caption ( '**Figura 1:** Histograma de frecuencia de sismo en función de la profundidad de los focos sísmicos.' )    
    st . write ( '**Según magnitud:**' )
    st . descuento ( "###" )
    bar_chart  =  df_catalogo . MAGNITUD . value_counts ()
    gráfico_de_barras  =  pd . Marco de datos ( bar_chart )
    gráfico_de_barras . columnas  = [ 'Magnitud del sismo' ]
    st . gráfico_de_barras ( gráfico_de_barras )
    st . caption ( '**Figura 2:** Histograma de frecuencia de sismo en función del rango de magnitud.' )  
    
#---------------------------MAPAS------------------------------------- ----------
df_local = pd . read_excel ( "Catálogo.xlsx" )
df_intermedia  =  pd . read_csv ( "https://raw.githubusercontent.com/heidi1904/programaci-n/main/intermedia.xlsx%20-%20catalogo.csv" )

si se  selecciona  ==  'Mapas' :
    st . markdown ( "<h1 style ='text-align: center'>Mapa sísmico del Perú</h1>" , unsafe_allow_html = True )
    st . descuento ( '____' )
    st . write ( "Un mapa sísmico representa la distribución espacial de los eventos sísmicos que dieron lugar en el Perú. La información obtenida fue a partir de la Plataforma Nacional de Datos Abiertos extraídos del Instituto Geofísico del Perú (IGP). Los sismos fueron clasificados según su profundidad: Superficiales, Intermedios y Profundos." )
    imagen  =  Imagen . abrir ( 'Mapa_sismico.jpg' )
    st . imagen ( imagen )
    st . escribe ( "**Fuente:** MINAM " )
    st . descuento ( '____' )
    st . escribe ( '''El Dr. Hernando Tavera, investigador científico en sismología y geofísica, también director de la Subdirección de Ciencias de la Tierra Sólida (SCTS) del Instituto Geofísico del Perú (IGP); destaca que esta información es de vital importancia para que las municipalidades tomen las medidas de prevención necesarias para reducir el Riesgo de Desastres Naturales ante peligros inminentes como los sismo e inundaciones.
“El mapa muestra la distribución espacial de todos los sismos ocurridos desde el año 1960… con magnitudes mayores y/o iguales a 4.0 Mw. Estos eventos fueron clasificados en función de la profundidad a la cual ocurren en superficiales, intermedios y profundos, remarcando que en el país los sismos están presentes hastaes del orden de profundidad de 700 km”, dijo.
''' )
    imagen  =  Imagen . abierto ( 'Imagen_Dr.jpg' )
    st . imagen ( imagen )
    st . write ( "**Fuente:** Instituto Geofísico del Perú" )
    st . descuento ( '____' )
    #df_local=pd.read_csv("https://raw.githubusercontent.com/heidi1904/programaci-n/main/Catalogo.xlsx%20-%20Catalogo1960_2021.csv")
    @ calle . cache
    def  localización_datos ():
        df_local  =  pd . read_excel ( 'Catálogo.xlsx' )
        df_local  =  df_local . renombrar ( columnas = {
                'LATITUD' : 'lat' ,
                'LONGITUD' : 'lon' ,
            })
        volver  df_local
    datos  =  localización_datos ()
    
    dato1 = dato [ dato [ "PROFUNDIDAD" ] <= 60 ]
    #dato2=dato[dato["PROFUNDIDAD"]<=300]
    mapa_datos = datos1 [[ "lat" , "lon" ]]
    

    conjunto de datos  =  st . cuadro de selección (
        'Seleccione una opción:' ,
        ( 'Profundidad superficial' ,
         'Profundidad intermedia' ,
         'Profundidad profunda' )
        )
    opción  =  '-'
    if  dataset  ==  'Profundidad superficial' :
        option  =  'profundidad superficial'
        st . descuento ( "###" )
        st . subheader ( '**Sismos registrados con ' + opción + ' durante 1960-2021.**' )
     
    
    elif  dataset  ==  'Profundidad intermedia' :
        option  =  'profundidad intermedia'
        st . descuento ( "###" )
        st . subheader ( '**Sismos registrados con ' + opción + ' durante 1960-2021.**' )
        @ calle . cache
        def  intermedia_data ():
            df_intermedia  =  pd . read_excel ( 'intermedia.xlsx' )
            df_intermedia  =  df_intermedia . renombrar ( columnas = {
                'LATITUD' : 'lat' ,
                'LONGITUD' : 'lon' ,
            })
            devolver  df_intermedia
        datos  =  intermedia_datos ()
        st . mapa ( datos )
        st . descuento ( "###" )
        st . marco de datos ( df_intermedia )
        cant  =  len ( df_intermedia . ejes [ 0 ])
            

    elif  dataset  ==  'Profundidad profunda' :
        option  =  'profundidad profunda'
        st . descuento ( "###" )
        st . subheader ( '**Sismos registrados con ' + opción + ' durante 1960-2021.**' )
       
    
     
    st . write ( 'Se encontraron' , cant , 'registros de sismos para su búsqueda.' )
    st . mapa ( mapa_datos )
    

       
    

#----------------------------EQUIPO------------------- ---------    
si se  selecciona  ==  'Equipo' :
    st . markdown ( "<h1 style ='text-align: center'>¿Quiénes somos?</h1>" , unsafe_allow_html = True )
    st . descuento ( '____' )
    st . write ( "Somos un grupo de estudiantes del 5to ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia (UPCH), buscamos que el usuario que ingrese a nuestra página pueda revisar de forma sencilla la magnitud que registraron los sismo entre los años 1960 y 2021 mediante un salpicadero." )
    imagen  =  Imagen . abierto ( 'Foto grupal.jpg' )
    st . imagen ( imagen )
