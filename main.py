from fastapi import FastAPI
import pandas as pd

from src.utils import utils
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Cargar los datos
steam_games = pd.read_pickle("./data/steam_games.pkl")
user_reviews = pd.read_pickle("./data/user_reviews.pkl")
users_items = pd.read_pickle("./data/users_items.pkl")


# Crear una matriz de utilidad a partir de la tabla de usuarios e items
matrix_utility = users_items.pivot(
    index='item_id', columns='user_id', values='playtime_forever').fillna(0)

# Convertir la matriz de utilidad a una matriz sparse para mejorar la eficiencia
matrix_utility_sparse = csr_matrix(matrix_utility.values)

model_knn = NearestNeighbors(
    metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)

# Entrenar el modelo
model_knn.fit(matrix_utility_sparse)

app = FastAPI()

@app.get("/developer/{desarrollador}")
async def get_developer_info(desarrollador: str):
    result = utils.developer_info(desarrollador, steam_games)
    return result

@app.get("/user-data/{user_id}")
async def get_user_data(user_id: str):
    result = utils.user_data(user_id, user_reviews, users_items)
    return result

@app.get("/user-for-genre/{genre}")
async def get_user_for_genre(genre: str):
    result = utils.user_for_genre(genre, steam_games, users_items)
    return result

@app.get("/best-developer-year/{year}")
async def get_best_developer_year(year: int):
    result = utils.best_developer_year(year, steam_games, user_reviews)
    return result

@app.get("/developer-reviews-analysis/{desarrolladora}")
async def get_developer_reviews_analysis(desarrolladora: str):
    result = utils.developer_reviews_analysis(desarrolladora, steam_games, user_reviews)
    return result

@app.get("/recomendacion-juego/{item_id}")
async def get_recomendacion_juego(item_id: str):
    result = utils.recomendacion_juego(item_id, steam_games, matrix_utility, model_knn, k=5)
    return result
