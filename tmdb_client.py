import requests
import os
key = os.environ.get("TMDB_API_TOKEN", "")

params = {"api_key": key}

def call_tmdb_api(endpoint):
   target = f"https://api.themoviedb.org/3/{endpoint}"
   response = requests.get(target, params=params)
   response.raise_for_status()
   return response.json()

def get_poster_url(poster_api_path, size="w342"):
    #func tht makes url for movie poster
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(type):
   return call_tmdb_api(f"movie/{type}")

def get_popular_movies(how_many, type):
    #func that limits r.json cause its huge
    r = get_movies(type)
    movies = r['results'][:how_many]
    return movies

def get_single_movie(movie_id):
   return call_tmdb_api(f"movie/{movie_id}")

def get_movie_credits(movie_id):
   return call_tmdb_api(f"movie/{movie_id}/credits")

def search(search_query):
    result = call_tmdb_api(f"search/movie?query={search_query}")
    return result['results']

def get_airing_today(how_many):
    result =  call_tmdb_api(f"tv/airing_today")
    return result['results'][:how_many]

"""def get_movie_credits(movie_id):
    #func tht gets credits of movie
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    r = requests.get(endpoint, params=params)
    return r.json()"""

"""def search(search_query):
    #func tht search for movies
    endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}"
    r = requests.get(endpoint, params=params)
    result = r.json()
    return result['results']"""

"""def get_single_movie(movie_id):
    #func tht gets single movie details
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, params=params)
    return response.json()"""

"""def get_movies(type):
    #func tht downloads most popular movies from tmdb API
    target = f"https://api.themoviedb.org/3/movie/{type}"
    r = requests.get(target, params=params)
    r.raise_for_status()
    return(r.json())"""

"""def get_airing_today(how_many):
    #func tht gets series airing today in TV
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    r = requests.get(endpoint, params=params)
    result = r.json()
    return result['results'][:how_many]"""