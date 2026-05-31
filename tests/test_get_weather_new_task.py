import pytest
import requests
from unittest.mock import patch

from src.utils.get_weather_new_task import get_coords, get_weather

@patch('src.utils.get_weather_new_task.requests.get')
def test_get_coords(mock_get, monkeypatch):

    monkeypatch.setattr(
        'src.utils.get_weather_new_task.API_KEY',
        'test_api_key'
    )

    import src.utils.get_weather_new_task as module

    print(module.API_KEY)

    mock_response = mock_get.return_value

    mock_response.json.return_value = [
        {
            'lat': 53.9024716,
            'lon': 27.5618225
        }
    ]

    coords = get_coords('Minsk')

    assert coords == (53.9024716, 27.5618225)

    mock_response.raise_for_status.assert_called_once()

    mock_get.assert_called_once_with(
        'http://api.openweathermap.org/geo/1.0/direct',
        params={
            'q': 'Minsk',
            'appid': 'test_api_key',
        }
    )


@patch('src.utils.get_weather_new_task.requests.get')
def test_get_coords_error(mock_get, monkeypatch):
    monkeypatch.setattr(
        'src.utils.get_weather_new_task.API_KEY',
        'test_api_key'
    )

    mock_get.return_value.json.return_value = []


    with pytest.raises(ValueError):
        get_coords('123')


def test_get_coords_without_api_key(monkeypatch):
    monkeypatch.setattr(
        'src.utils.get_weather_new_task.API_KEY',
        None
    )

    with pytest.raises(ValueError):
        get_coords('Minsk')

@patch('src.utils.get_weather_new_task.requests.get')
def test_get_weather(mock_get, monkeypatch):
    monkeypatch.setattr(
        'src.utils.get_weather_new_task.API_KEY',
        'test_api_key'
    )

    mock_response = mock_get.return_value

    mock_response.json.return_value = {
        'main': {
            'temp': 9.83,
        }
    }

    assert get_weather(1, 1) == 9.83

    mock_response.raise_for_status.assert_called_once()

    mock_get.assert_called_once_with(
        'https://api.openweathermap.org/data/2.5/weather',
        params = {
        'lat': 1,
        'lon': 1,
        'appid': 'test_api_key',
        'units': 'metric',
        'lang': 'ru',
    },
        timeout=10
    )

def test_get_weather_with_missing_api_key(monkeypatch):
    monkeypatch.setattr(
        'src.utils.get_weather_new_task.API_KEY',
        None
    )

    with pytest.raises(ValueError, match='API_KEY not set'):
        get_weather(1, 1)
