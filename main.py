import pandas as pd 
from fastapi import FastAPI
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

app.title = "Proyecto individial 01, funciones"

#http://127.0.0.1:8000
@app.get("/")
def index():
    return "funciona"


df_funciones = pd.read_parquet("df_funciones.parquet")
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes):
    
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}
    
    mes = mes.lower()
    mes_numero = meses.get(mes)
    
    if mes_numero is None:
        return "El mes ingresado no es válido. Por favor, ingrese un mes en español."
    cantidad = df_funciones[df_funciones['release_date'].dt.month == mes_numero].shape[0]
    
    return f"{cantidad} películas fueron estrenadas en el mes de {mes.capitalize()}."

print(cantidad_filmaciones_mes("marzo"))



@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia):
    
    dias_semana = {
        'lunes': 0, 'martes': 1, 'miércoles': 2, 'jueves': 3, 
        'viernes': 4, 'sábado': 5, 'domingo': 6
    }
    dia = dia.lower()
    dia_numero = dias_semana.get(dia)
    
    if dia_numero is None:
        return "El día ingresado no es válido. Por favor, ingrese un día de la semana en español."
    cantidad = df_funciones[df_funciones['release_date'].dt.dayofweek == dia_numero].shape[0]
    return f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}."


print(cantidad_filmaciones_dia("sábado"))




@app.get("/score_titulo/{titulo_de_la_filmacion}")
def score_titulo(titulo_de_la_filmacion: str):

    titulo_formateado = titulo_de_la_filmacion.lower().replace("_", " ")
    pelicula = df_funciones[df_funciones['title'].str.lower() == titulo_formateado]
    
    if pelicula.empty:
        return "No se encontró una película con ese título."
    
    titulo = pelicula['title'].values[0]
    año = pelicula['release_year'].values[0]
    score = pelicula['popularity'].values[0]  

    return f"La película '{titulo}' fue estrenada en el año {año} con un score/popularidad de {score}."

print(score_titulo("The Empire Strikes Back"))



@app.get("/votos_titulo/{titulo_de_la_filmacion}")
def votos_titulo(titulo_de_la_filmacion):
    
    titulo_formateado = titulo_de_la_filmacion.replace("_", " ").lower()
    pelicula = df_funciones[df_funciones['title'].str.lower() == titulo_formateado]
    if pelicula.empty:
        return "No se encontró una película con ese título."
    
    titulo = pelicula['title'].values[0]
    año = pelicula['release_year'].values[0]
    votos = pelicula['vote_count'].values[0]
    promedio_votos = pelicula['vote_average'].values[0]
    if votos < 2000:
        return f"La película '{titulo}' no cumple con el mínimo de 2000 valoraciones (actual: {votos})."
    
    return f"La película '{titulo}' se estrenó en el año {año}, cuenta con un total de {votos} valoraciones, con un promedio de {promedio_votos}."

print(votos_titulo("Alien:_Covenant"))


#modelo de recomendacion usando similitud de coseno. 


df_funciones['combined_features'] = df_funciones['genres_name'] + ' ' + df_funciones['belongs_to_collection_name'] + ' ' + df_funciones['overview']
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df_funciones['combined_features'].fillna(''))  

#  Función de recomendación
@app.get("/recomendacion/{titulo}")
def recomendacion(titulo):
    
    if titulo not in df_funciones['title'].values:
        return "La película no se encuentra en el dataset."
    idx = df_funciones[df_funciones['title'] == titulo].index[0]
    
    cosine_similarities = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_similarities.argsort()[-6:-1][::-1]  
    recommended_titles = df_funciones.iloc[similar_indices]['title'].tolist()
    
    return recommended_titles


pelicula_input = "from russia with love"  
recomendaciones = recomendacion(pelicula_input)
print(f"Películas recomendadas para '{pelicula_input}':", recomendaciones)