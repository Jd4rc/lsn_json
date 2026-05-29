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

    for user in data:
        if 'age' not in user:
            raise KeyError('Invalid user data')
        if not isinstance(user['age'], int):
            raise TypeError('Age must be an integer')


    ages = [el['age'] for el in data]

    if not ages:
        raise ValueError('Users list is empty')


    average = sum(ages) / len(ages)

    return average
