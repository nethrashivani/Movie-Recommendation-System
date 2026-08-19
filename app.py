import pickle
import streamlit as st
import requests
from sklearn.metrics.pairwise import cosine_similarity


def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path

    return None


movies = pickle.load(open("model/movie_list.pkl", "rb"))
vector = pickle.load(open("model/vector.pkl", "rb"))


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]

    distances = cosine_similarity(vector[index], vector).flatten()

    movie_indices = distances.argsort()[::-1][1:6]

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movie_indices:
        movie_id = movies.iloc[i].movie_id

        recommended_movie_names.append(movies.iloc[i].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


st.header("Movie Recommender System")

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            if poster:
                st.image(poster)