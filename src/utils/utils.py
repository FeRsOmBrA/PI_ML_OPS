import gzip 
import pandas as pd 
import json
import ast

def cargar_json_gz(ruta_archivo, way ):
    """
    Carga un archivo JSON en formato GZ y devuelve un DataFrame.
    
    Parámetros:
    - ruta_archivo: Ruta del archivo JSON comprimido en formato GZ.
    - way: Forma de cargar el archivo, si es 0 se carga con gzip/json, si es 1 se carga con gzip/ast.
    
    Retorna:
    - DataFrame: Un DataFrame que contiene los datos del archivo JSON.
    """
    if way  == 0:
      with gzip.open(ruta_archivo, 'r') as archivo_gz:
          datos = [json.loads(linea) for linea in archivo_gz]
      return pd.DataFrame(datos)
    else :
        contenido = [] 
        for i in gzip.open(ruta_archivo):
            contenido.append(ast.literal_eval(i.decode("utf-8")))
        return pd.DataFrame(contenido)
             
def developer_info(desarrollador: str, steam_games_df):
    """
    Obtiene información sobre los juegos desarrollados por un desarrollador específico.

    Args:
        desarrollador (str): El nombre del desarrollador.
        steam_games_df (pandas.DataFrame): El DataFrame que contiene los datos de los juegos de Steam.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa información sobre los juegos lanzados por el desarrollador.
              Cada diccionario contiene las siguientes claves:
    """
    # Filtrar juegos por desarrollador
    dev_games = steam_games_df[steam_games_df['developer'] == desarrollador]
    # Agrupar por año y contar juegos
    games_per_year = dev_games.groupby('release_year').agg(
        {'app_name': 'count', 'price': lambda x: (x == 0).mean()})
    games_per_year.rename(columns={'app_name': 'Cantidad de Juegos',
                          'price': 'Porcentaje Juegos Gratuitos'}, inplace=True)
    games_per_year['Porcentaje Juegos Gratuitos'] = games_per_year['Porcentaje Juegos Gratuitos'] * 100
    return games_per_year.reset_index().to_dict('records')


def user_data(user_id: str, user_reviews_df, user_items_df):
    """
    Calcula información sobre un usuario específico.

    Args:
        user_id (str): El ID del usuario.
        user_reviews_df: El dataframe de las reseñas de los usuarios.
        user_items_df: El dataframe de los items del usuario.

    Returns:
        dict: Un diccionario con la información del usuario, incluyendo el ID del usuario,
        el dinero gastado (simulado), el porcentaje de recomendación y la cantidad de items.
    """    
    # Calcular el gasto total del usuario
    user_games = user_items_df[user_items_df['user_id'] == user_id]
    # Simulación del gasto total
    total_spent = user_games['playtime_forever'].sum()

    # Calcular el porcentaje de recomendación
    user_recommendations = user_reviews_df[user_reviews_df['user_id'] == user_id]
    recommend_percentage = (user_recommendations['recommend'].mean()) * 100

    # Contar la cantidad de items
    items_count = user_games.shape[0]

    return {
        "Usuario": user_id,
        # Asumiendo que el gasto se relaciona con las horas de juego
        "Dinero gastado": f"{total_spent} horas (simulado)",
        "Porcentaje de recomendación": f"{recommend_percentage:.2f}%",
        "Cantidad de items": items_count
    }

def user_for_genre(genre: str, steam_games_df, user_items_df):
    """
    Encuentra el usuario con más horas jugadas para un género específico.

    Args:
        genre (str): El género específico.
        steam_games_df: El DataFrame de juegos de Steam.
        user_items_df: El DataFrame de los juegos jugados por los usuarios.

    Returns:
        dict: Un diccionario que contiene el usuario con más horas jugadas para el género y las horas jugadas por año.
    """
    # Filtrar juegos por género
    genre_games = steam_games_df[steam_games_df['genres'].str.contains(
        genre, case=False, na=False)]

    # Unir con user_items para obtener los juegos jugados por los usuarios que coinciden con el género
    genre_user_items = user_items_df.merge(
        genre_games, left_on='item_id', right_on='id')

    # Agrupar por usuario y sumar el tiempo de juego total
    user_playtime = genre_user_items.groupby(
        'user_id')['playtime_forever'].sum().reset_index()

    # Encontrar el usuario con más tiempo de juego
    top_user = user_playtime.loc[user_playtime['playtime_forever'].idxmax()]

    # Filtrar los juegos jugados por el top user y agrupar por año
    top_user_games = genre_user_items[genre_user_items['user_id']
                                      == top_user['user_id']]
    hours_played_by_year = top_user_games.groupby(
        'release_year')['playtime_forever'].sum().reset_index()

    return {
        "Usuario con más horas jugadas para Género": top_user['user_id'],
        "Horas jugadas": hours_played_by_year.to_dict('records')
    }
def best_developer_year(year: int, steam_games_df, user_reviews_df):
    """
    Devuelve los tres desarrolladores con más recomendaciones positivas en juegos lanzados en un año específico.

    Parámetros:
    - year: int, el año para el cual se desea obtener los mejores desarrolladores.
    - steam_games_df: DataFrame, el DataFrame que contiene la información de los juegos de Steam.
    - user_reviews_df: DataFrame, el DataFrame que contiene las reseñas de los usuarios.

    Retorna:
    - top_3_developers: list, una lista de diccionarios que contiene los tres desarrolladores con más recomendaciones positivas,
                        junto con la cantidad de recomendaciones que han recibido.
    """
    
    # Filtrar juegos por año
    year_games = steam_games_df[steam_games_df['release_year'] == year]
    
    # Unir con user_reviews para obtener las reseñas de los juegos de ese año
    reviews_year_games = user_reviews_df.merge(year_games, left_on='item_id', right_on='id')
    
    # Filtrar por recomendaciones positivas
    positive_reviews = reviews_year_games[reviews_year_games['recommend'] == True]
    
    # Agrupar por desarrollador y contar las recomendaciones
    developer_recommendations = positive_reviews.groupby('developer')['recommend'].count().reset_index()
    
    # Ordenar y obtener el top 3
    top_3_developers = developer_recommendations.sort_values(by='recommend', ascending=False).head(3)
    
    return top_3_developers.to_dict('records')


def developer_reviews_analysis(desarrolladora: str, steam_games_df, user_reviews_df):
    """
    Analiza las reseñas de los juegos de un desarrollador específico.

    Args:
        desarrolladora (str): El nombre del desarrollador.
        steam_games_df (DataFrame): El DataFrame que contiene la información de los juegos de Steam.
        user_reviews_df (DataFrame): El DataFrame que contiene las reseñas de los usuarios.

    Returns:
        dict: Un diccionario que contiene el recuento de reseñas positivas y negativas para el desarrollador especificado.
            Ejemplo: {'desarrolladora': {'Negative': 10, 'Positive': 20}}
    """
    # Filtrar los juegos por el desarrollador
    dev_games = steam_games_df[steam_games_df['developer'] == desarrolladora]
    
    # Unir con user_reviews para obtener las reseñas de los juegos de ese desarrollador
    dev_reviews = user_reviews_df.merge(dev_games, left_on='item_id', right_on='id')
    
    # Contar las reseñas positivas y negativas
    sentiment_count = dev_reviews['sentiment_analysis'].value_counts()
    
    # Preparar el resultado
    result = {
        desarrolladora: {
            'Negative': sentiment_count.get(0, 0),  # Si no hay reseñas negativas, retorna 0
            'Positive': sentiment_count.get(2, 0)   # Si no hay reseñas positivas, retorna 0
        }
    }
    
    return result

def recomendacion_juego(item_id, steam_games_df, matrix_utility, model_knn, k=5):
    item_id_str = str(item_id)

    if item_id_str not in steam_games_df['id'].astype(str).values:
        return f"El juego con ID {item_id} no fue encontrado."

    try:
        item_idx = matrix_utility.index.get_loc(item_id_str)
        distances, indices = model_knn.kneighbors(
            matrix_utility.iloc[item_idx, :].to_numpy().reshape(1, -1), n_neighbors=k+1)

        recommended_ids = [matrix_utility.index[i]
                           for i in indices.flatten()[1:]]
        recomendaciones = []

        for rec_id in recommended_ids:
            if rec_id in steam_games_df['id'].astype(str).values:
                nombre_juego = steam_games_df[steam_games_df['id'].astype(
                    str) == rec_id]['app_name'].iloc[0]
                recomendaciones.append({'id': rec_id, 'nombre': nombre_juego})
            else:
                recomendaciones.append(
                    {'id': rec_id, 'nombre': 'Nombre de juego no encontrado'})

        return recomendaciones
    except Exception as e:
        return str(e)  # Devolver el mensaje de error


