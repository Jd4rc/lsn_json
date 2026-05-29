import datetime


def get_days_between_dates(
        date1: str,
        date2: str
) -> int:
    """
    Возвращает разницу в днях между двумя датами.

    :param date1: Первая дата в формате DD.MM.YYYY.
    :param date2: Вторая дата в формате DD.MM.YYYY.
    :return: Разница между датами в днях.
    """
    start_date  = datetime.datetime.strptime(date1, '%d.%m.%Y')
    end_date  = datetime.datetime.strptime(date2, '%d.%m.%Y')

    result = end_date - start_date

    return result.days