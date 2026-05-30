import pytest
import requests
from unittest.mock import patch

from src.utils.get_weather_new_task import get_coords

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