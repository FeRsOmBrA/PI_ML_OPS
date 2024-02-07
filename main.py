from fastapi import FastAPI
import pandas as pd

from src.utils import utils
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import pickle
# Cargar los datos
steam_games = pd.read_pickle("./data/steam_games.pkl")
user_reviews = pd.read_pickle("./data/user_reviews.pkl")
users_items = pd.read_pickle("./data/users_items.pkl")
matrix_utility = pickle.load(open("./data/matrix_utility.pkl", "rb"))
model_knn = pickle.load(open("./data/model_knn.pkl", "rb"))
steam_games_model = pickle.load(open("./data/steam_games_model.pkl", "rb"))

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
    result = utils.recomendacion_juego(item_id, steam_games_model, matrix_utility, model_knn, k=5)
    return result
