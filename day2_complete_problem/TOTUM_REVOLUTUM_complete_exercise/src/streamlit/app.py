import streamlit as st
from PIL import Image
import json
import requests
import pandas as pd
from sqlalchemy import create_engine

# Haz que se pueda importar correctamente estas funciones que están en la carpeta utils/

import os,sys

dir = os.path.dirname

path1 = dir(dir(os.path.abspath(__file__)))
sys.path.append(path1)


from utils_.stream_config import draw_map
from utils_.dataframes import load_csv_for_map

menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Load Image", "Map", "API", "Australia fires", "Machine Learning"])

if menu == "No selected": 

    settings_file = dir(dir(dir(os.path.abspath(__file__)))) + os.sep + "config" + os.sep + "config.json"
    with open(settings_file, "r") as json_file_readed: 
        json_readed = json.load(json_file_readed)

    # Pon el título del proyecto que está en el archivo "config.json" en /config
    st.title(json_readed["Title"])
    # Pon la descripción del proyecto que está en el archivo "config.json" en /config
    st.write(json_readed["Description"])
    
if menu == "Load Image": 

    # Carga la imagen que está en data/img/happy.jpg
    imagen = Image.open(dir(dir(dir(os.path.abspath(__file__)))) + os.sep + 'data' + os.sep + "img" + os.sep + 'happy.jpg')
    st.image (imagen,use_column_width=True)

if menu == "Map":

    # El archivo que está en data/ con nombre 'red_recarga_acceso_publico_2021.csv'
    csv_map_path = dir(dir(dir(os.path.abspath(__file__)))) + os.sep + 'data' + os.sep + "red_recarga_acceso_publico_2021.csv"
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

if menu == "API":
    r = requests.get("http://localhost:6060/").json()
    df = pd.DataFrame(r)
    st.write(df)

if menu == "Australia fires":
    
    from utils_.sql_functions import load_sql
    st.write(load_sql())

if menu == "Machine Learning":

    from utils_.ml import gridSearch

    st.write(gridSearch())



    
    # 1. Conecta a la BBDD


    # 2. Obtén, a partir de sentencias SQL (no pandas), la información de las tablas que empiezan por 'fire_archive*' (join)
    # 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    # 4. Añade una entrada en la tabla 'student_findings' por cada uno de los tres modelos. 'student_id' es EL-ID-DE-TU-GRUPO.
    # 5. Obtén la información de la tabla 'fire_nrt_M6_96619' y utiliza el mejor modelo para predecir la columna target de esos datos. 
    # 6. Usando SQL (no pandas) añade una columna nueva en la tabla 'fire_nrt_M6_96619' con el nombre 'fire_type_EL-ID-DE-TU-GRUPO'
    # 7. Muestra por pantalla en Streamlit la tabla completa (X e y)




