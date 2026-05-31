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


def get_weather(
        lat:float,
        lon:float,
) -> float:
    """
    Получает текущую температуру воздуха по заданным координатам
    через API OpenWeatherMap.

    Args:
        lat: Широта местоположения.
        lon: Долгота местоположения.

    Returns:
        Температура воздуха в градусах Цельсия.

    Raises:
        ValueError: Если переменная окружения API_KEY не задана.
        requests.exceptions.RequestException:
            Если запрос к API завершился ошибкой.
        KeyError:
            Если в ответе API отсутствуют ожидаемые данные.
    """
    if not API_KEY:
        raise ValueError("API_KEY not set")

    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    return data['main']['temp']

