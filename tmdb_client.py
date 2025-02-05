import requests

key = "500f36ef896a715b62b47503917bb44f"
params = {"api_key": key}

def get_poster_url(poster_api_path, size="w342"):
    #func tht makes url for movie poster
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(type):
    #func tht downloads most popular movies from tmdb API
    target = f"https://api.themoviedb.org/3/movie/{type}"
    r = requests.get(target, params=params)
    r.raise_for_status()
    return(r.json())

def get_popular_movies(how_many, type):
    #func that limits r.json cause its huge
    r = get_movies(type)
    movies = r['results'][:how_many]
    return movies

def get_single_movie(movie_id):
    #func tht gets single movie details
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, params=params)
    return response.json()

def get_movie_credits(movie_id):
    #func tht gets credits of movie
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    r = requests.get(endpoint, params=params)
    return r.json()

def search(search_query):
    #func tht search for movies
    endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}"
    r = requests.get(endpoint, params=params)
    result = r.json()
    return result['results']