import json
import pathlib
from datetime import datetime

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


def event_duration(filename: str) -> list[int]:
    file_path = BASE_DIR / 'data' / filename

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    durations = []

    for event in data:
        start_date = datetime.strptime(
            event['start_date'], '%Y-%m-%d'
        )

        end_date = datetime.strptime(
            event['end_date'], '%Y-%m-%d'
        )

        duration = (end_date - start_date).days

        durations.append(duration)

    return durations


