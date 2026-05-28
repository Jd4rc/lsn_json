from src.utils.datetime123 import add_week_to_dates

def test_add_week_to_dates():
    dates = ["2022.12.31", "2023.1.7"]

    result = add_week_to_dates(dates)

    assert result == [
        "January 7, 2023",
        "January 14, 2023"
    ]



