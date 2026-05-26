import os
from pathlib import Path
from dotenv import load_dotenv
import json
import requests

BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(BASE_DIR / '.env')
API_KEY = os.getenv('API_KEY')

def get_coords(city: str) -> tuple:
    geo_url = 'http://api.openweathermap.org/geo/1.0/direct'

    geo_params = {
        'q': city,
        'appid': API_KEY,
        'limit': 1
    }

    try:
        geo_response = requests.get(geo_url, params=geo_params)

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data:
            print("Город не найден")
            exit()

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

    except requests.exceptions.RequestException as error:
        print("Request failed: ", error)
        exit()

    return (lat, lon)

def get_weather(lat:float, lon:float) -> float:

    weather_url = 'https://api.openweathermap.org/data/2.5/weather'

    weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        weather_response = requests.get(weather_url, params=weather_params)

        weather_response.raise_for_status()

        weather_data = weather_response.json()


    except requests.exceptions.RequestException as error:
        print("Request failed: ", error)
        exit()

    return weather_data['main']['temp']


# from unittest.mock import patch
#
# def get_github_user_info(username):
#     response = requests.get(f'https://api.github.com/users/{username}')
#     return response.json()
#
# @patch('requests.get')
# def test_get_github_user_info(mock_get):
#     mock_get.return_value.json.return_value = {
#         'login': 'testuser', 'name': 'Test User'
#     }
#     assert (
#             get_github_user_info('testuser') ==
#             {'login': 'testuser', 'name': 'Test User'}
#     )
#     mock_get.assert_called_once_with(
#         'https://api.github.com/users/testuser'
#     )

