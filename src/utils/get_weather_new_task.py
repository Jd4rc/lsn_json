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
    if not API_KEY:
        raise Exception("API_KEY not set")

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    lat = data[0]['lat']
    lon = data[0]['lon']

    return (lat, lon)

