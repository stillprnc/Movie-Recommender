import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2c33a4af99a3552462bf28e2be585a0d&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = " http://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    topFiveSimilarMovie = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies_name = []
    recommended_movies_poster = []
    for i in topFiveSimilarMovie:
        movie_id = movies.iloc[i[0]]['movie_id'] 
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommend_movies_name.append(movies.iloc[i[0]]['title'])
    return recommend_movies_name, recommended_movies_poster
        

st.header("Movies Recommendation System Using ML")
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values

st.markdown("**Type or select a movie to get recommendation**")

# selected_movie stores the movie the user pick 
selected_movie = st.selectbox(
    '', 
    movie_list
)

if st.button('Show recommendation'):
    recommended_movies_names, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_poster[0], use_container_width=True) 
    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_poster[1], use_container_width=True)
    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_poster[2], use_container_width=True)
    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_poster[3], use_container_width=True)
    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_poster[4], use_container_width=True)