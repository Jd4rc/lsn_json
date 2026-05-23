from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        print(f"Обработано: {len(result)} элементов")

        return result
    return wrapper