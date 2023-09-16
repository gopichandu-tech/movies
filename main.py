import background
import streamlit as st
import pickle as pk
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=69f61e0f48863d371425c9be43548704&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend_movie(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommend = []
    recommend_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend.append(movies.iloc[i[0]].title)
        # fetching the poster from the api
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend,recommend_movies_poster

movies_dict = pk.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pk.load(open('similarity.pkl','rb'))
st.title("Movies Recommended System")
selected_movie_name = st.selectbox(
    "Name a Movie Our AI Recommends Similar Movies",
    (movies['title'].values)
)

#Button
if st.button('Recommend Movie'):
    movie_names,movie_posters = recommend_movie(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])
    st.header("Enjoy the day!")


