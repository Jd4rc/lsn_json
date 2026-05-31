# Weather API Project

Учебный Python-проект для получения текущей температуры воздуха по названию города с использованием OpenWeatherMap API.

## Описание

Проект позволяет:

* получить координаты города по его названию;
* получить текущую температуру воздуха по координатам;
* получить температуру воздуха сразу по названию города.

Проект создан для практики работы с:

* HTTP-запросами;
* библиотекой `requests`;
* переменными окружения;
* обработкой ошибок;
* тестированием с `pytest`;
* моками через `unittest.mock`.

## Основные функции

### `get_coords(city: str) -> tuple[float, float]`

Получает широту и долготу города через OpenWeatherMap Geocoding API.

### `get_weather(lat: float, lon: float) -> float`

Получает текущую температуру воздуха по координатам.

### `get_weather_by_city(city: str) -> float`

Получает координаты города и возвращает текущую температуру воздуха.

## Установка

Клонируйте репозиторий:

```bash
git clone <https://github.com/Jd4rc/lsn_json.git>
cd <Weather API Project>
```

Установите зависимости:

```bash
poetry install
```

## Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
API_KEY=your_openweathermap_api_key
```

Получить API-ключ можно на сайте OpenWeatherMap.

## Пример использования

```python
from src.utils.get_weather_new_task import get_weather_by_city

temperature = get_weather_by_city("Minsk")

print(f"Текущая температура: {temperature} °C")
```

## Запуск тестов

```bash
pytest
```

Запуск тестов с отчетом о покрытии:

```bash
pytest --cov=src
```

HTML-отчет о покрытии:

```bash
pytest --cov=src --cov-report=html
```

После выполнения команды отчет будет находиться в папке `htmlcov`.

## Что покрыто тестами

В проекте протестированы:

* успешное получение координат города;
* ситуация, когда город не найден;
* отсутствие `API_KEY`;
* успешное получение температуры;
* ошибка HTTP-запроса;
* некорректный JSON-ответ от API;
* связка функций `get_coords()` и `get_weather()` через `get_weather_by_city()`.

## Стек

* Python
* Requests
* Pytest
* Poetry
* python-dotenv
* unittest.mock
