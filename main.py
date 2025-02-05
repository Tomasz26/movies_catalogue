from flask import Flask, render_template, url_for, request
import requests
import json
import tmdb_client
import random
import datetime

app = Flask(__name__)
movie_list = ['popular', 'top_rated', 'upcoming', 'now_playing']

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in movie_list:
        selected_list = 'popular'
    movies = tmdb_client.get_popular_movies(8, type = selected_list)
    random.shuffle(movies)
    
    return render_template("homepage.html", movies=movies, movie_list=movie_list, list_type = selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    credits = tmdb_client.get_movie_credits(movie_id)
    cast = credits.get('cast', [])
    return render_template("movie_details.html", movie=details, cast = cast)

@app.route("/search")
def search():
    search_query = request.args.get("q", "")
    if search_query:
        searched = tmdb_client.search(search_query)
    else:
        searched = []
    return render_template("search.html", searched = searched, search_query = search_query)

@app.route("/today")
def airtoday():
    movies = tmdb_client.get_airing_today(8)
    today = datetime.date.today()
    return render_template("today.html", movies = movies, today = today)