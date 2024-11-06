


      
![image](https://github.com/user-attachments/assets/f7f9a055-4f4a-47c1-8a05-b9758c3ee26c)
 
# Proyecto individual 01
# Machine learning operations (MLOps)

## Descripcion del proyecto 

- Este proyecto tiene como objetivo desarrollar un sistema de recomendacion de peliculas basado en tecnicas de **machine learning**, que ofrece una experiencia de recomendacion  personalizada tomando tu historial de peliculas como referencia. 

**Tabla de contenido**
1.
2.
3.

## instalacion y requisitos 
**Requisitos**
**pasos de instalacion**

## ETL
**Transformaciones**

Como se puede observar en el [ETL.ipynb][id/name], Se realizo un preprocesamiento y transformacion de datos para poder trabajar con la propuesta planteada. 

## propuesta de trabajo 

* Algunos campos, como **belongs_to_collection**, **production_companies** y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

* Los valores nulos de los campos **revenue**, **budget** deben ser rellenados por el número 0.

* Los valores nulos del campo **release date** deben eliminarse.

* De haber fechas, deberán tener el formato **AAAA-mm-dd**, además deberán crear la columna **release_year** donde extraerán el año de la fecha de estreno.

* Crear la columna con el **retorno de inversión**, llamada **return** con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

* Eliminar las columnas que no serán utilizadas:  **video, imdb_id, adult, original_title, poster_path y homepage**.

**Transformaciones adicionales**
- En la columna **"popularity"** se convierten los datos a tipo string.
- Se crea un nuevo DF que solo contiene solo las columnas nesesarias para las funciones y el modelo de recomendacion, al cual se le llamo **"df_funciones"**.
- Se convierte en **archivo.parquet** para optimizacion de espacio en memoria para render. 

## EDA, Análisis exploratorio de los datos.  
Con los datos limpios y las tranformaciones realizadas ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets y ver si hay algún patrón interesante que valga la pena explorar. Acontinuacion se muestran los graficos utilizados para la exploracion: 

Se crea una nube de palabras con el fin de ayudar al sistema de recomendacion, ya que es una representación gráfica en la que el tamaño de cada palabra refleja su frecuencia en el texto, de forma que ayuda a identificar rápidamente temas y términos recurrentes.

![image](https://github.com/user-attachments/assets/6c1f194b-7bb8-46db-acfd-a709f2e562f4)



Grafico de barras que representa la relacion en la columna 'belongs_to_collection_name' contando cuántas películas pertenecen a cada colección, con la intencion de dar una idea de qué colecciones son más populares.
![image](https://github.com/user-attachments/assets/479bab25-0463-403b-9687-48c90ca093c6)



Grafico de barras que representa la frecuencia de generos en peliculas. 
![image](https://github.com/user-attachments/assets/72e7b5ad-3ddc-445c-a83f-9ad911d59e17)





## API y funciones en render. 
Deben crear 4 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).

**def cantidad_filmaciones_mes( Mes )**: Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

   
   *Ejemplo de retorno: x cantidad de peliculas fueron estrenadas en el mes de x* 

**def cantidad_filmaciones_dia( Dia )**: Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.


  *Ejemplo de retorno: x cantidad de peliculas fueron estrenadas en los dias x*
                    

**def score_titulo( titulo_de_la_filmación )**: Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.


  *Ejemplo de retorno: La pelicula x fu estrenada en el año x con un score de x*
                   
                    
**def votos_titulo( titulo_de_la_filmación )**: Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.


  *Ejemplo de retorno: la pelicula x fue estrenada en el año x. La misma cuenta con un total de x valoraciones, con un promedio de x* 



  ## Sistema de recomendacion  
Una vez que toda la data es consumible por la API, se crea un sistema de recomendacion utilizando el modelo de **similitud del coseno** queconsiste en recomendar películas a los usuarios basándose en películas similares. Estas se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. 

**def recomendacion( titulo )**: Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.



## Repositorio

* main.py : Archivo principal donde podemos ver las funciones y el sistema de recomendacion de similitud del coseno utilizada en el desarrollo de la API. 
* requirements.txt: Archivo con todas las librerias que se utilizaron en el proyecto. 
* ETL.ipynb: Notebook detallado con el proceso de extraccion, transformacion y carga. 
* EDA.ipynb: Notebook detallado con el proceso de limpieza de datos. 




## Links y accesos rapidos

[API ](https://proyecto-01-recomendacion-de-peliculas.onrender.com)- Aqui podras encontrar las funciones que se despliegan en render. 

[video explicacion ](https://www.youtube.com/watch?v=-bsR86aNKEs)- Explicacion en youtube de las APIS 

**contacto**: Martha Vasquez. 




 
 

                


