import streamlit as st
import pickle

movie_data = pickle.load(open('movie_data.pkl','rb'))
similar_movie = pickle.load(open('similar_movie.pkl','rb'))
list_movies = movie_data['title'].values


st.title('Movie Recommender System')
movie_name = st.selectbox('Choose the movie name from the list' , (list_movies))


def recommend(movie_name):
    movie_idx = movie_data[movie_data['title'] == movie_name].index[0]
    similar_movies = similar_movie[movie_idx]
    movie_list = sorted(enumerate(similar_movies), reverse=True, key=lambda x: x[1])[1:6]

    recommended_list = []
    for i in movie_list:
        recommended_list.append(movie_data.loc[i[0]].values[1])
    return recommended_list


if st.button('Recommend'):
    recommended = recommend(movie_name)
    for _list in recommended:
        st.write(_list)

