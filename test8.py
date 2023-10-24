import pytest
import json
import main8
# from main8 import get_user_info, User

# Загрузка данных из существующего файла json
@pytest.fixture(scope='module')
def users_data_load():
    with open('users.json') as file:
        data = json.load(file)
    return data

# Проверка доступа пользователя
def test_user_access(users_data_load):
    for user in users_data_load:
        assert 'access_level' in user

# Проверка наличия id пользователя
def test_user_id(users_data_load):
    for user in users_data_load:
        assert 'id' in user

# Проверка наличия имени пользователя
def test_user_name(users_data_load):
    for user in users_data_load: 
        assert 'name' in user

# Проверка правильности формата данных пользователя
def test_user_data_format(users_data_load):
    for user in users_data_load:
        assert isinstance(user['access_level'], int)
        assert isinstance(user['id'], int)
        assert isinstance(user['name'], str)

if __name__ == '__main__':
    pytest.main(['-v'])

print(users_data_load())