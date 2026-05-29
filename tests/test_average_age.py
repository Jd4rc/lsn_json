import json
import pytest
from src.utils.average_age import get_average_age


def test_get_average_age(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / 'name_and_age.json'

    test_data = [
        {"name": "Alex", "age": 20},
        {"name": "Bob", "age": 25},
        {"name": "Kate", "age": 18}
    ]

    file_path.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        'src.utils.average_age.BASE_DIR',
        tmp_path,
    )

    average_age = get_average_age('name_and_age.json')

    assert average_age == 21.0


def test_get_average_age_with_no_data(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / 'name_and_age.json'

    test_data = []

    file_path.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        'src.utils.average_age.BASE_DIR',
        tmp_path,
    )

    with pytest.raises(ValueError):
        get_average_age('name_and_age.json')

def test_get_average_age_with_invalid_data(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / 'name_and_age.json'

    test_data = [
        {'123': '123', '456': '456'},
        {'Bob': 'Bob', '123': '123', '456': '456'},
        {'Kate': 123},
    ]

    file_path.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        'src.utils.average_age.BASE_DIR',
        tmp_path,
    )

    with pytest.raises(KeyError):
        get_average_age('name_and_age.json')



def test_get_average_age_with_age_type_str(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / 'name_and_age.json'

    test_data = [
        {"name": "Alex", "age": "20"},
        {"name": "Bob", "age": "25"},
        {"name": "Kate", "age": "18"}
    ]

    file_path.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        'src.utils.average_age.BASE_DIR',
        tmp_path,
    )

    with pytest.raises(TypeError):
        get_average_age('name_and_age.json')
