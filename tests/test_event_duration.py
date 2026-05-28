import json
import pytest
from src.utils.event_duration import event_duration


def test_event_duration(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    events_file = data_dir / "events.json"

    events = [
        {
            "start_date": "2023-01-01",
            "end_date": "2023-01-05",
        },
        {
            "start_date": "2023-02-10",
            "end_date": "2023-02-20",
        },
    ]

    events_file.write_text(
        json.dumps(events),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.utils.event_duration.BASE_DIR",
        tmp_path,
    )

    result = event_duration("events.json")

    assert result == [4, 10]


def test_event_duration_empty_file(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    events_file = data_dir / "events.json"
    events_file.write_text("[]", encoding="utf-8")

    monkeypatch.setattr(
        "src.utils.event_duration.BASE_DIR",
        tmp_path,
    )

    result = event_duration("events.json")

    assert result == []

def test_event_duration_invalid_date(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    events_file = data_dir / "events.json"

    events = [
        {
            "start_date": "01-01-2023",
            "end_date": "2023-01-05",
        }
    ]

    events_file.write_text(
        json.dumps(events),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.utils.event_duration.BASE_DIR",
        tmp_path,
    )

    with pytest.raises(ValueError):
        event_duration("events.json")