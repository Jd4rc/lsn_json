import json
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


def event_duration(filename: str) -> list[int]:
    file_path = BASE_DIR / 'data' / filename

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

data = event_duration('events.json')

print(data)
