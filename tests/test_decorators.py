import pytest

from src.utils.decorators import log


def test_log_returns_original_result():
    @log
    def get_items():
        return [1, 2, 3]

    result = get_items()

    assert result == [1, 2, 3]

def test_log_prints_count_of_items(capsys):
    @log
    def get_items():
        return ["a", "b", "c"]

    get_items()

    captured = capsys.readouterr()

    assert captured.out == "Обработано: 3 элементов\n"
