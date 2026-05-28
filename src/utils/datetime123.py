from datetime import datetime, timedelta


# date_obj = datetime.datetime.now()

# print(date_obj)
# print(date_obj.year)
# print(date_obj.month)
# print(date_obj.day)
#
# date_str = date_obj.strftime('%Y')
#
# print(date_str)


def add_week_to_dates(
        dates: list[str]
) -> list[str]:
    output_dates = []
    for date in dates:
        date_obj = datetime.strptime(date, '%Y.%m.%d')
        new_date_obj = date_obj + timedelta(days=7)
        output_dates.append(new_date_obj.strftime('%B %#d, %Y'))
    return output_dates

print(add_week_to_dates(["2022.12.31", "2023.1.7"]))






