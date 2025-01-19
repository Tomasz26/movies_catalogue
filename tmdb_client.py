import requests

def get_poster_url(poster_api_path, size="w342"):
    #func tht makes url for movie poster
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies():
    #func tht downloads most popular movies from tmdb API
    key = '500f36ef896a715b62b47503917bb44f'
    target = 'https://api.themoviedb.org/3/movie/popular'
    params = {"api_key": key}
    r = requests.get(target, params=params)
    return(r.json())

def get_popular_movies(how_many):
    #func that limits r.json cause its huge
    r = get_movies()
    movies = r['results'][:how_many]
    return movies