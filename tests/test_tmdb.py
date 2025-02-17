import tmdb_client
import requests

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def get_movies_list(list_type):
   endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(endpoint, headers=headers)
   response.raise_for_status()
   return response.json()

def test_get_movies_type_popular():
   movies_list = tmdb_client.get_movies(type="popular")
   assert movies_list is not None
