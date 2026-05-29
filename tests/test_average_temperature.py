import json

from src.utils.average_temperature import (
    save_average_temperature, calculate_average_temperature
)

def test_calculate_average_temperature(tmp_path, monkeypatch):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()

    file_path = data_dir / 'weather_for_task.json'

    test_data = {
        'Moscow': {
            '2024-01-01': 10,
            '2024-01-02': 20,
            '2024-01-03': 30,
        }
    }

    file_path.write_text(
        json.dumps(test_data),
        encoding='utf-8',
    )

    monkeypatch.setattr(
        'src.utils.average_temperature.BASE_DIR',
        tmp_path,
    )

    result = calculate_average_temperature(
        'weather_for_task.json',
        'Moscow',
    )

    assert result == {
        'Moscow': 20.0
    }



