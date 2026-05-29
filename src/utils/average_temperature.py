import pathlib
import json
BASE_DIR = pathlib.Path(__file__).parent.parent.parent


def calculate_average_temperature(
        filename: str,
        city: str
) -> dict:
    file_path = BASE_DIR / 'data' / filename
    with open(
            file_path,
            encoding='utf-8'
    ) as f:
        data = json.load(f)

    temperatures = data[city].values()

    avg_temperature = sum(temperatures) / len(temperatures)

    return {
        city: avg_temperature
    }


def save_average_temperature(
        result: dict,
) -> None:

    output_path = BASE_DIR / 'data' / 'output.json'

    with open(
            output_path,
            'w',
            encoding='utf-8'
    ) as f:
        json.dump(
            result, f, indent=4, ensure_ascii=False
        )



average_temperature = calculate_average_temperature(
        'weather_for_task.json',
        "Moscow"
)

