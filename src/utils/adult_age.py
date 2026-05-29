import pathlib
import json
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

def get_adults(
        filename:str
) -> list[dict]:
    """
        Возвращает список совершеннолетних пользователей из JSON-файла.

        Пользователь считается совершеннолетним, если его возраст
        больше либо равен 18 годам.

        Args:
            filename: Имя JSON-файла с данными пользователей.

        Returns:
            Список словарей с данными совершеннолетних пользователей.

        Raises:
            ValueError: Если в данных пользователя отсутствует ключ 'age'.
    """
    file_path = BASE_DIR / 'data' / filename

    data = json.loads(
        file_path.read_text(
            encoding='utf-8'
        )
    )


    for el in data:
        if 'age' not in el:
            raise ValueError('Invalid user data')

    return [
        el
        for el in data
        if el['age'] >= 18
    ]


print(get_adults('name_and_age.json'))