import pytest
from unittest.mock import Mock
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

def test_call_tmdb_api_gives_proper_result(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.call_tmdb_api(endpoint="tv/airing_today")
    assert movies_list == mock_movies_list

def test_get_single_movie_gives_proper_result(monkeypatch):
    mock_movie_data = {"id": 1234, "title": "Mocked Movie 2"}

    call_tmdb_api_mock = Mock(return_value=mock_movie_data)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    result = tmdb_client.get_single_movie(123)
    assert result == mock_movie_data

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
