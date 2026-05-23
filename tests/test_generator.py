from src.utils.generator import generate_users


def test_generate_users_return_dict(data):
    generator = generate_users(data['first_names'], data['last_names'], data['cities'])

    user = next(generator)

    assert isinstance(user, dict)

def test_generate_users_has_reqiured_fields(data):
    generator = generate_users(data['first_names'], data['last_names'], data['cities'])

    user = next(generator)

    assert list(user.keys()) == ['first_name', 'last_name', 'age', 'city']


def test_generate_users_values_from_list(data):
    generator = generate_users(data['first_names'], data['last_names'], data['cities'])

    user = next(generator)

    assert user['first_name'] in data['first_names']
    assert user['last_name'] in data['last_names']
    assert user['city'] in data['cities']


def test_generate_users_age_between_18_65(data):
    generator = generate_users(data['first_names'], data['last_names'], data['cities'])

    user = next(generator)

    assert 18 <= user["age"] <= 65
