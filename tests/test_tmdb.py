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

def test_call_tmdb_api_handles_http_error(monkeypatch):
    response_mock = Mock()
    response_mock.raise_for_status.side_effect = requests.exceptions.HTTPError("Mocked HTTP error")

    mock_requests_get = Mock(return_value = response_mock)
    monkeypatch.setattr("tmdb_client.requests.get", mock_requests_get)

    with pytest.raises(requests.exceptions.HTTPError, match="Mocked HTTP error"):
        tmdb_client.call_tmdb_api("movie/popular")

def test_get_single_movie_gives_proper_result(monkeypatch):
    mock_movie_data = {"id": 1234, "title": "Mocked Movie 2"}

    call_tmdb_api_mock = Mock(return_value=mock_movie_data)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    result = tmdb_client.get_single_movie(1234)
    assert result == mock_movie_data

    call_tmdb_api_mock.assert_called_once_with("movie/1234")

def test_get_movie_credits_gives_proper_result(monkeypatch):
    mock_credits_data = {"name": "Peter Parker", "character": "Spiderman"}

    call_tmdb_api_mock = Mock(return_value=mock_credits_data)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    result = tmdb_client.get_movie_credits(1234)
    assert result == mock_credits_data

    call_tmdb_api_mock.assert_called_once_with("movie/1234/credits")

def test_get_movies_type_popular():
   movies_list = tmdb_client.get_movies(type="popular")
   assert movies_list is not None
