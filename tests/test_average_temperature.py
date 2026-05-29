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

def test_save_average_temperature(tmp_path, monkeypatch):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()

    monkeypatch.setattr(
        'src.utils.average_temperature.BASE_DIR',
        tmp_path,
    )

    result = {
        'Moscow': 20.0
    }

    save_average_temperature(result)

    output_path = data_dir / 'output.json'

    assert output_path.exists()

    saved_data = json.loads(
        output_path.read_text(encoding='utf-8'),
    )

    assert saved_data['Moscow'] == 20.0


