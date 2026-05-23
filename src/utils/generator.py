import random


def generate_users(first_names, last_names, cities):
    """
    Генерирует словарь с пользователем. Имеет следущие параметры:
    :param first_names: хз
    :param last_names: хз
    :param cities: хз
    :return: хз
    """
    while True:
        user = {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "age": random.randint(18, 65),
            "city": random.choice(cities),
        }
        yield user
