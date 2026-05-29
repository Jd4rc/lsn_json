from src.utils.days_between_dates import get_days_between_dates


def test_days_between_dates():
    result = get_days_between_dates(
        '01.01.2022',
        '31.01.2022'
    )

    assert result == 30

def test_get_days_between_same_date():
    result = get_days_between_dates(
        '01.01.2022',
        '01.01.2022',
    )

    assert result == 0


