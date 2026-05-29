import datetime


def get_days_between_dates(
        date1: str,
        date2: str
) -> int:
    date1 = datetime.datetime.strptime(date1, '%d.%m.%Y')
    date2 = datetime.datetime.strptime(date2, '%d.%m.%Y')

    result = date2 - date1

    return result.days

print(get_days_between_dates("01.01.2022", "31.01.2022"))