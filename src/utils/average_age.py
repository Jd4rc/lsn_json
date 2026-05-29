import json
import pathlib
BASE_DIR = pathlib.Path(__file__).parent.parent.parent


def get_average_age(
        filename: str
) -> float|int:
    file_path = BASE_DIR / 'data' / filename

    data = json.loads(
    file_path.read_text(
        encoding='utf-8'
    )
)


    ages = [el['age'] for el in data]

    average = sum(ages) / len(ages)

    return average
