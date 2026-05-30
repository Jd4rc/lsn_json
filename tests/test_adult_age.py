import json
import pytest
from src.utils.adult_age import get_adults

def test_get_adults(tmp_path, monkeypatch):
    data_path = tmp_path / "data"
    data_path.mkdir()

    file_path = data_path / 'name_and_age.json'

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
        'src.utils.adult_age.BASE_DIR', tmp_path
    )

    adults = get_adults('name_and_age.json')

    assert adults == test_data


def test_get_adults_with_invalid_data(tmp_path, monkeypatch):
    data_path = tmp_path / "data"
    data_path.mkdir()

    file_path = data_path / 'name_and_age.json'

    test_data = [
        {"name": "Alex", "city": 'St.Petersburg'},
        {"name": "Bob", "city": 'California'},
        {"name": "Kate", "city": 'Moscow'}
    ]

    file_path.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        'src.utils.adult_age.BASE_DIR', tmp_path
    )

    with pytest.raises(ValueError):
        get_adults('name_and_age.json')