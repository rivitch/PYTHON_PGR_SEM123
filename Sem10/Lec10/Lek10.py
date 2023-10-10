# data = list((1, 2, 3))
# print(f'{data = }, {type(data) = }, {type(list) = }')

"""data = [1, 2, 3], type(data) = <class 'list'>, type(list) = <class 'type'>"""

#==============
# import random
# import supermodule

# # supermodule.py  - пользовательский модуль
# result1 = random.randint(1, 10)       # точечная 
# result2 = supermodule.randint(60)     # нотация 
# print(result2)

"""
1696915987.146849
25
1696916831.8635695
11
1696916858.7271059
38
1696916872.6088998
52
"""
#===============================
# class MyBestSuperData:    # класс
#     max_up = 3      # Атрибут класса       
# p1 = MyBestSuperData()    # Экземляры 
# p2 = MyBestSuperData()    # класса
# print(f'{MyBestSuperData.max_up = }, {p1.max_up = }, {p2.max_up = }')
# p1.max_up = 12            # смена значения атрибута внутри экземпляра, атрибут класса не меняется
# print(f'{MyBestSuperData.max_up = }, {p1.max_up = }, {p2.max_up = }')
# MyBestSuperData.max_up = 42   # # смена значения атрибута класса, атрибут внутри экземпляра p2 не меняется
# print(f'{MyBestSuperData.max_up = }, {p1.max_up = }, {p2.max_up = }')
# """
# MyBestSuperData.max_up = 3, p1.max_up = 3, p2.max_up = 3
# MyBestSuperData.max_up = 3, p1.max_up = 12, p2.max_up = 3
# MyBestSuperData.max_up = 42, p1.max_up = 12, p2.max_up = 42
# """

# # ===========================


# MyBestSuperData.level = 1   # Добавляем атрибут класса через точку
# print(f'{MyBestSuperData.level = }, {p1.level = }, {p2.level = }') # новый атрибут класса появился у экземпляров
# """
# MyBestSuperData.level = 1, p1.level = 1, p2.level = 1
# """
# p1.health = 100    # Добавляем атрибут экземпляра через точку
# #print(f'{MyBestSuperData.health = }, {p1.health = }, {p2.health = }') # Ошибка - в классе нет такого атрибута
# """

# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem10/Lek10", line 47, in <module>
#     print(f'{MyBestSuperData.health = }, {p1.health = }, {p2.health = }') # AttributeError: type object 'Person' has no attribute 'health'
# AttributeError: type object 'MyBestSuperData' has no attribute 'health'
# """
# #print(f'{p1.health = }, {p2.health = }') # # Ошибка - Ни класс, ни экземпляр p2 не могут получить доступ к данному атрибуту.
# """
# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem10/Lek10", line 58, in <module>
#     print(f'{p1.health = }, {p2.health = }') # AttributeError: 'Person' object has no attribute 'health'
# AttributeError: 'MyBestSuperData' object has no attribute 'health'
# """
# print(f'{p1.level = }, {p1.health = }')  # Доступ к новому атрибуту имеет только сам экземпляр.
# """
# MyBestSuperData.max_up = 3, p1.max_up = 3, p2.max_up = 3
# MyBestSuperData.max_up = 3, p1.max_up = 12, p2.max_up = 3
# MyBestSuperData.max_up = 42, p1.max_up = 12, p2.max_up = 42
# MyBestSuperData.level = 1, p1.level = 1, p2.level = 1
# p1.level = 1, p1.health = 100
# """
# #============================
# # аналог работы со словарями dict.

# dict_p1 = {}
# dict_p1['level'] = 2
# dict_p1['health'] = 200
# print(f'{p1.health = }')
# print(f'{dict_p1["health"] = }')
# print(f'{p1.health = }')
# print(f'{dict_p1}')
# """
# p1.health = 100
# dict_p1["health"] = 200
# p1.health = 100
# {'level': 2, 'health': 200}
# """
# #===========================
# # Научный тык

# # a = {key: value for key, value in enumerate(p1)} # ошибка
# # print(a)
# """
# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem10/Lek10", line 83, in <module>
#     a = {key: value for key, value in enumerate(p1)}
# TypeError: 'MyBestSuperData' object is not iterable
# """
# # MyBestSuperData.health = 300
# # a = {key: value for key, value in enumerate(MyBestSuperData)} # ошибка
# # print(a)
# """
# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem10/Lek10", line 98, in <module>
#     a = {key: value for key, value in enumerate(MyBestSuperData)} # ошибка
# TypeError: 'type' object is not iterable
# """

# #print({p1})

# -==========================+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class Person:
#     max_up = 3
#     def __init__(self):       
#         self.level = 1         # аргументы экемпляров
#         self.health = 100      # аргументы экемпляров
#         print(f'{id(self) = }')
# p1 = Person()
# print(f'{id(p1) = }')
# p2 = Person()
# print(f'{id(p2) = }')
# """
# id(self) = 30976320
# id(p1) = 30976320
# id(self) = 30976080
# id(p2) = 30976080
# """
# print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
# print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# # print(f'{Person.max_up = }, {Person.level = }, {Person.health = }') # AttributeError: type object 'Person' has no attribute 'level'
# Person.level = 100
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')
# """
# p1.max_up = 3, p1.level = 1, p1.health = 100
# p2.max_up = 3, p2.level = 1, p2.health = 100
# Person.level = 100, p1.level = 1, p2.level = 1
# """
#===========================
# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):  # unknown
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'1. {p1.name = }, {p1.race = }')
# print(f'2. {p2.name = }, {p2.race = }')
# print(f'3. {p3.name = }, {p3.race = }')
# """
# p1.name = 'Сильвана', p1.race = 'Эльф'
# p2.name = 'Иван', p2.race = 'Человек'
# p3.name = 'Грогу', p3.race = 'unknown'
# """
# #------------------------------------
# class Person:
#     max_up1 = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#     def level_up(self):
#         self.level += 1
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity    
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'4. {p1.level = }, {p2.level = }, {p3.level = }')
# p3.level_up()   # p3 +1 = 2
# p1.level_up()   # p1 +1 = 2
# p3.level_up()   # p3 +1 = 3
# print(f'5. {p1.level = }, {p2.level = }, {p3.level = }')
# #print(f'6. {Person.max_up = }') # Класс перезаписан - ошибка
# """
# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem10/Lek10", line 176, in <module>
#     print(f'6. {Person.max_up = }') # Класс перезаписан - ошибка
# AttributeError: type object 'Person' has no attribute 'max_up'
# """
# print(f'6. {Person.max_up1 = }')
# """
# 1. p1.name = 'Сильвана', p1.race = 'Эльф'
# 2. p2.name = 'Иван', p2.race = 'Человек'
# 3. p3.name = 'Грогу', p3.race = 'unknown'
# 4. p1.level = 1, p2.level = 1, p3.level = 1
# 5. p1.level = 2, p2.level = 1, p3.level = 3
# 6. Person.max_up1 = 3
# """
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# p1.change_health(p2, 10)  # вызов метода класса 
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# """
# p1.health = 100, p2.health = 100, p3.health = 100
# p1.health = 110, p2.health = 90, p3.health = 100
# """
#+++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++
class User:
    count = []
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
u1 = User('One', '123-45-67')
u2 = User('NoOne', '76-54-321')
u1.count.append(42)  # u1(42)
u1.count.append(73)  # u1(42, 73)
u2.counter = 256
u2.count.append(u2.counter)  # u2(256)
u2.count.append(u1.count[-1])# u2(256, 73)
print(f'{u1.name = }, {u1.phone = }, {u1.count = }')   # u1.name = 42, u1.phone = 73, u1.count = 'One'
print(f'{u2.name = }, {u2.phone = }, {u2.count = }')   # u2.name = 256, u1.phone = 73, u1.count = 'One'
"""
u1.name = 'One', u1.phone = '123-45-67', u1.count = [42, 73, 256, 256]
u2.name = 'NoOne', u2.phone = '76-54-321', u2.count = [42, 73, 256, 256]
"""
