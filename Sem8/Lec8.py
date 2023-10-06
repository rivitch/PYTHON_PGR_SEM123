

import json
import csv


with open('Sem8/user8.json', 'r', encoding='utf-8') as f:   # пЕРВАЯ ПАПКА
    json_file = json.load(f)
print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')
#    +++++++++++++++
# json_text = """
# [
# {
# "userId": 1,
# "id": 9,
# "title": "nesciunt iure omnis dolorem tempora et accusantium",
# "body": "consectetur animi nesciunt iure dolore"
# },
# {
# "userId": 1,
# "id": 10,
# "title": "optio molestias id quia eum",
# "body": "quo et expedita modi cum officia vel magni"
# },
# {
# "userId": 2,
# "id": 11,
# "title": "et ea vero quia laudantium autem",
# "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
# },
# {
# "userId": 2,
# "id": 12,
# "title": "in quibusdam tempore odit est dolorem",
# "body": "praesentium quia et ea odit et ea voluptas et"
# }
# ]"""
# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')
#+++++++++++++++++++++++++++++++
# my_dict = {
# "first_name": "Джон",
# "last_name": "Смит",
# "hobbies": ["кузнечное дело", "программирование",
# "путешествия"],
# "age": 35,
# "children": [
# {
# "first_name": "Алиса",
# "age": 5
# },
# {
# "first_name": "Маруся",
# "age": 3
# }
# ]
# }
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('Sem8/new_user8.json', 'w', encoding='utf-8') as f:  
#     json.dump(my_dict, f, ensure_ascii=False) #  ensure_ascii=False
#+++++++++++++++++++++++++++++++++++++++++++++++++++

# my_dict = {
# "id": 123,
# "name": "Clementine Bauche",
# "username": "Cleba",
# "email": "cleba@corp.mail.ru",
# "address": {
# "street": "Central",
# "city": "Metropolis",
# "zipcode": "123456"
# },
# "phone": "+7-999-123-45-67"
# }
# res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
# print(res)
#==================================
# a = 'Hello world!'
# b = {key: value for key, value in enumerate(a)}   # Красиво...
# c = json.dumps(b, indent=3, separators=('; ', '= '))
# print(c)
#================================

# with open('Sem8/csv8.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
# with open('Sem8/csv_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)  # Чето толком не работает, все по разному
#     for line in csv_file:
#         print(line)
# print(type(line))
# ++++++++++++++++++++++++++++++++++++

# with (                                                         
#     open('csv_tab.csv', 'r', newline='') as f_read,
#     open('new_csv_tab.csv', 'w', newline='', encoding='utf-8') as f_write
# ):                                # скобки работают только с верси 3.9
with open('Sem8/csv_tab.csv', 'r', newline='') as f_read:
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    
#f_read.close()   
with open('Sem8/new_csv_tab.csv', 'w', newline='', encoding='utf-8') as f_write:      
        #csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', quotechar='|', quoting=csv.QUOTE_MINIMAL) #, delimiter=''
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line[2] += 1
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            all_data.append(line)
    csv_write.writerows(all_data)




#-------------
# PS I:\GB\TASKS\PYTHON_PGR_SEM123> & i:/GB/TASKS/PYTHON_PGR_SEM123/.virt/Scripts/python.exe i:/GB/TASKS/PYTHON_PGR_SEM123/Sem8/Lec8.py
# type(json_file) = <class 'dict'>
# json_file = {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': ['Shanna@melissa.tv', 'antonette@howel.com'], 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}
# json_file["name"] = 'Ervin Howell'
# json_file["address"]["geo"] = {'lat': '-43.9509', 'lng': '-34.4618'}
# json_file["email"] = ['Shanna@melissa.tv', 'antonette@howel.com']