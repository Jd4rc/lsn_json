import requests
import pathlib
from dotenv import load_dotenv
import os

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')
API_KEY = os.getenv("API_KEY")



def get_coords(
        city:str
) -> tuple[float, float]:
    """
       Получает географические координаты указанного города.

       Выполняет запрос к OpenWeather Geocoding API и возвращает
       широту и долготу первого найденного результата.

       Args:
           city: Название города для поиска.

       Returns:
           Кортеж из двух чисел типа float:
           (широта, долгота).

       Raises:
           ValueError: Если API_KEY не задан.
           ValueError: Если город не найден.
           requests.exceptions.RequestException:
               Если запрос к API завершился ошибкой.
       """
    if not API_KEY:
        raise ValueError("API_KEY not set")

    url = 'http://api.openweathermap.org/geo/1.0/direct'

    params = {
        'q': city,
        'appid': API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError('City not found')

    return data[0]['lat'], data[0]['lon']
