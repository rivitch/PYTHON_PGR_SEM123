import json
import pytest

def get_user_info():
  try:
    with open('users.json', 'r') as file:
      user_data = json.load(file)
  except FileNotFoundError:
    user_data = {}
    
    while True:
      name = input("Введите имя: ")
      id = input("Введите идентификатор: ")
      level =0
      while int(level) < 1 or int(level) > 7:
         level = input("Введите уровень доступа (от 1 до 7): ")
         print("Попробуйте снова.")
      level = int(level)
      user_data.setdefault(level, {})
      user_data[level][id] = name
      #print("Данные успешно сохранены.")
      choice = input("Хотите закончить ввод данных? (Y/N): ")
      if choice.lower() == "y":
        break
    with open('users.json', 'w') as file:
      json.dump(user_data, file)



class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level
    def read_json_file(file_path):
      with open(file_path) as file:
          data = json.load(file)
          for key in sorted(data):
              level = key
              for inner_key in sorted(data[key]):
                  identifier = inner_key
                  name = data[key][inner_key]
                  print(f"Уровень доступа: {level}, Идентификатор: {identifier}, Имя: {name}")

file_path = "users.json"
get_user_info()

User.read_json_file(file_path)

def users_data_load():
    with open('users.json') as file:
        data = json.load(file)
        print(data)
    return data

@pytest.fixture # (scope='module')# scope='module'
def users_data_load():
    with open('users.json') as file:
        data = json.load(file)
        print(data)
    return data
    #print(users_data_load())

# Доступ пользователя
def test_access(data):
    for level in data:
        assert int(level) >7,"!" 
#     # for level in data:
#     #     assert level<1 or level>7, "!"
#         # if level<1 or level>7:
#         #     assert 'level' in data, "!"
#         # print(level)
#         # assert 'level' in data
#         # print("Доступ разрешен")
#     #return f'Доступ {level} у пользователя {user}'    

# # id пользователя
# def test_id(data):
#     for id in data:
#         assert 'id' in data

# # Пользователь
# def test_user(data):
#     for user in data:
#         assert 'user' in data

# # файл json
# def test_file():
#     try:
#         with open('users.json') as file:
#             pass
#     except FileNotFoundError:
#         pytest.fail("Файл users.json не найден")

# if __name__ == '__main__':
#     pytest.main(['-v'])
users_data_load()