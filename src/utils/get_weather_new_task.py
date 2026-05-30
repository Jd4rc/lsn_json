import requests
import pathlib
from dotenv import load_dotenv
import os

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')
API_KEY = os.getenv("API_KEY")



def get_coord(
        city:str
) -> tuple[float, float]:
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}'
    response = requests.get(url)

    data = response.json()

    lat = data[0]['lat']
    lon = data[0]['lon']

    return (lat, lon)

