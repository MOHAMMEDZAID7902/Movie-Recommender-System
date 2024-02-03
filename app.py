import streamlit as st
import pickle
import pandas as pd
import requests
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://s2.r29static.com/bin/entry/2ab/0,791,5615,2948/x,80/1650643/image.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def fetch_overview(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5d6f0074aecae4f922faf0408316e95&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return data['overview']

def fetch_vote(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5d6f0074aecae4f922faf0408316e95&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return data['vote_count']

def fetch_average(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5d6f0074aecae4f922faf0408316e95&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return data['vote_average']

def fetch_popular(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5d6f0074aecae4f922faf0408316e95&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return data['popularity']
def fetch_language(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5d6f0074aecae4f922faf0408316e95&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return data['original_language']
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5d6f0074aecae4f922faf0408316e95&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_overview = []
    recommended_movies_vote = []
    recommended_movies_count = []
    recommended_movies_popular = []
    recommended_movies_language = []
    for i in movie_list:
        id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(id))
        recommended_movies_overview.append(fetch_overview(id))
        recommended_movies_language.append(fetch_language(id))
        recommended_movies_vote.append(fetch_vote(id))
        recommended_movies_count.append(fetch_average(id))
        recommended_movies_popular.append(fetch_popular(id))
    return recommended_movies,recommended_movies_posters, recommended_movies_overview,recommended_movies_language,recommended_movies_vote,recommended_movies_count, recommended_movies_popular


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommendation System')

similarity = pickle.load(open('similarity.pkl','rb'))

Selected_Movie= st.selectbox("Enter Movie Name: ", movies['title'].values)


if st.button('Recommend'):
    names,posters,overview,lang,vote,count,pop = recommend(Selected_Movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(names[0])
        st.image(posters[0])
        st.divider()
        st.write("Overview")
        st.caption(overview[0])
        st.write("Language")
        st.caption(lang[0])
        st.write("Vote Count")
        st.caption(vote[0])
        st.write("Vote Average")
        st.caption(count[0])
        st.write("Popularity")
        st.caption(pop[0])
        st.divider()
    with col2:
        st.subheader(names[1])
        st.image(posters[1])
        st.divider()
        st.write("Overview")
        st.caption(overview[1])
        st.write("Language")
        st.caption(lang[1])
        st.write("Vote Count")
        st.caption(vote[1])
        st.write("Vote Average")
        st.caption(count[1])
        st.write("Popularity")
        st.caption(pop[1])
        st.divider()
    with col3:
        st.subheader(names[2])
        st.image(posters[2])
        st.divider()
        st.write("Overview")
        st.caption(overview[2])
        st.write("Language")
        st.caption(lang[2])
        st.write("Vote Count")
        st.caption(vote[2])
        st.write("Vote Average")
        st.caption(count[2])
        st.write("Popularity")
        st.caption(pop[2])
        st.divider()
    with col4:
        st.subheader(names[3])
        st.image(posters[3])
        st.divider()
        st.write("Overview")
        st.caption(overview[3])
        st.write("Language")
        st.caption(lang[3])
        st.write("Vote Count")
        st.caption(vote[3])
        st.write("Vote Average")
        st.caption(count[3])
        st.write("Popularity")
        st.caption(pop[3])
        st.divider()
    with col5:
        st.subheader(names[4])
        st.image(posters[4])
        st.divider()
        st.write("Overview")
        st.caption(overview[4])
        st.write("Language")
        st.caption(lang[4])
        st.write("Vote Count")
        st.caption(vote[4])
        st.write("Vote Average")
        st.caption(count[4])
        st.write("Popularity")
        st.caption(pop[4])
        st.divider()
