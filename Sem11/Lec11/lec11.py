# #  Создание экземпляра класса, __init__

# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else[]
#         self.life = 3
#         # принтим только в учебных целях, а не для реальных задач
#         print(f'Создал {self} со свойствами:\n'
#             f'{self.name = },\t{self.equipment = },\t{self.life= }')
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'],
# name='Стэнц')
# print(f'{u_3.name}\t{u_3.life}')
#---------------------------

# Контроль создания класса через __new__(срабатывает один раз)

"""class A:
    def some_method(self):
        print('some_method A')
class B(A):
    def some_method(self):
        print('some_method B')

x = B()
print(x.some_method())"""

# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#         print({self})
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         print(f'Создал класс {cls}')
        
#         return instance
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман')
# print('Создаём третий раз')
# u_3 = User(name='Стэнц')

# ---
# Расширение неизменяемых классов  ?

# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a + b
# print(f'{c = }\t{type(c) = }')

# ------------------------

# Шаблон Одиночка, Singleton

# class Singleton:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self, name: str):
#         self.name = name
# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(a)   
# print(b)
# print(f'{a.name = }\n{b.name = }')  # один объект

# --------------------------
# Удаление экземпляра класса, __del__

# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __del__(self):                    # отрабатывает после достижения счетчика экземпляров нуля
#         print(f'Удаление экземпляра {self.name}')
# u_1 = User('Спенглер')
# u_2 = User('Венкман')


# import sys    # для работы со счетчиком, подсчет кол-ва ссылок у экземпляра
# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
# u_1 = User('Спенглер')
# print(sys.getrefcount(u_1))
# u_2 = u_1
# print(sys.getrefcount(u_1), sys.getrefcount(u_2))
# del u_1
# print(sys.getrefcount(u_2))
# # print(u_2.name)
# print('Завершение работы')
# print(sys.getrefcount(u_2))
# #print(u_2.name)
# # print(u_1.name)

#+++++++++++++++++++++++++++++++++
# Задание
# Перед вами несколько строк кода. Напишите что делает класс, не запуская код. У вас 3 минуты.
# class Count:    # шаблон "тройняшки"
#     _count = 0
#     _last = None
#     def __new__(cls, *args, **kwargs):
#         if cls._count < 3:
#             cls._last = super().__new__(cls)
#             cls._count += 1
#         return cls._last               # cls._last = None , cls._count = 1 , *args = name
#     def __init__(self, name: str):
#         self.name = name                  

"""

"""
# ========================
#2. Строка документации

# ---------------
# class User:
#     """A User training class for demonstrating class documentation.
#     Shows the operation of the help(cls) and the dander method __doc__"""
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
# u_1 = User('Спенглер')
# print('Справка класса User ниже', '*' * 50)
# help(User)
# print('Справка экземпляра u_1 ниже', '*' * 50)
# help(u_1)
#------
#Хранение документации в __doc__

# class User:
#     """A User training class for demonstrating class  documentation.
#     Shows the operation of the help(cls) and the dander method __doc__"""
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#         print(f'Создал {self.name = }')
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
# u_1 = User('Спенглер')
# print(f'Документация класса: {User.__doc__ = }')
# print(f'Документация экземпляра: {u_1.__doc__ = }')
# print(f'Документация метода: {u_1.simple_method.__doc__}')
#==========================
# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запускаякод. У вас 3 минуты.

# class MyClass:
#     A = 42
#     """About class"""
#     def __init__(self, a):   #, b
#         """self.__doc__ = None"""
#         self.a = a
#         #self.b = b   
#     def method(self, name):
#         """Documentation"""
#         self.__doc__ = None  # Документация для method стирается       
# # help(MyClass)
# u_1 = MyClass('Спенглер')
# print(f'Документация метода: {u_1.method.__doc__}')

"""
Документация метода: Documentation   # не стерлось ???
"""

# ==============================
# 3. Представления экземпляра

#----------------
# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()  # Метод capitalize() делает первую букву каждого слова заглавной/в принте не сработал?
# user = User('cпенглер')
# print(user)
# # print(user.name)
"""
<__main__.User object at 0x000000000257A940
"""


# -------
# Для получения читаемого описания необходимо переопределить как минимум один из дандер методов: __str__ или __repr__

#Представление для пользователя, __str__

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
# user = User('cпенглер')
# print(user)

# # ---
# """ Представление для создания экземпляра, __repr__"""
# #1
# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#     def __repr__(self):
#         return f'User({self.name})'
# user = User('Спенглер')
# print(user)

# # 2
# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else[]
#         self.life = 3
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)

#----------------------------
# 4. Приоритет методов
# 
# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else[]
#         self.life = 3
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)

# print(f'{user}')
# print(repr(user))
# print(f'{user = }')

# --------
# 5. Печать коллекций
# Однако метод __repr__ оказывается более приоритетным, если на печать выводится не один элемент, а коллекция элементов.

# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else[]
#         self.life = 3
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
# u_1 = User('Спенглер')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
# ghostbusters = [u_1, u_2, u_3]
# print(ghostbusters)
# print(f'{ghostbusters}')
# print(repr(ghostbusters))
# print(f'{ghostbusters = }')
# print(*ghostbusters, sep='\n')
# -------------

# # +++++++++++++++++
# # Задание
# # Перед вами несколько строк кода. Что в нём неправильно. У вас 3 минуты.
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.c = a + b
#     def __str__(self):
#         return f'MyClass(a={self.a}, b={self.b}, c={self.c})'
#     def __repr__(self):
#         return str(self.a) + str(self.b) + str(self.c)
#================================
# 6. Математика и логика в классах

# Сложение через __add__

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
# a = Vector(2, 4)
# b = Vector(3, 7)
# c = a + b
# print(f'{a = }\t{b = }\t{c = }')

#----
# Сдвиг вправо, __rshift__

# from random import choices
# class Closet:
#     CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')
#     def __init__(self, count: int, storeroom=None):
#         self.count = count
#         if storeroom is None:
#             self.storeroom = choices(self.CLOTHES, k=count)
#         else:
#             self.storeroom = storeroom
#     def __str__(self):
#         names = ', '.join(self.storeroom)
#         return f'Осталось вещей в шкафу {self.count}:\n{names}'
#     def __rshift__(self, other):
#         shift = self.count if other > self.count else other
#         self.count -= shift
#         return Closet(self.count, choices(self.storeroom, k=self.count))
# storeroom = Closet(10)
# print(storeroom)
# for i in range(4):
#     storeroom = storeroom >> 2
#     print(f'{i}, {storeroom}')
"""
Осталось вещей в шкафу 10:
туфли, перчатки, футболка, футболка, костюм, футболка, туфли, костюм, футболка, перчатки
0, Осталось вещей в шкафу 8:
костюм, футболка, футболка, футболка, футболка, перчатки, перчатки, костюм   # 3 футболки, 2 перчаток
1, Осталось вещей в шкафу 6:
перчатки, перчатки, футболка, перчатки, костюм, перчатки          # 1 футболка, 3 перчаток - откуда еще 1 перчатки???
2, Осталось вещей в шкафу 4:
футболка, костюм, перчатки, костюм
3, Осталось вещей в шкафу 2:
перчатки, футболка
"""

# -------
# 7. Right методы

# # Умножение текста на “продвинутый текст” методом __rmul__

# class StrPro(str):
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls, *args, **kwargs)
#         return instance
#     def __rmul__(self, other: str):
#         words = other.split()
#         result = self.join(words)
#         return StrPro(result)
# text = 'Каждый охотник желает знать где сидит фазан'
# s = StrPro(' (=^.^=) ')
# print(f'{text = }\n{s = }')
# print(text * s)       # ничивонипонял
# # print(s * text) # TypeError: 'str' object cannot be interpreted as an integer
"""
text = 'Каждый охотник желает знать где сидит фазан'
s = ' (=^.^=) '
Каждый (=^.^=) охотник (=^.^=) желает (=^.^=) знать (=^.^=) где (=^.^=) сидит (=^.^=) фазан
"""
# -------
# In place методы

# # Вычисление процентов вместо нахождения остатка от деления, __imod__
# from decimal import Decimal
# class Money:
#     def __init__(self, value: int or float):
#         self.value = Decimal(value)
#     def __repr__(self):
#         return f'Money({self.value:.2f})'   # :.2f - 2 знака после дроби (1.00)
#     def __imod__(self, other):
#         self.value = self.value * Decimal(1 + other / 100)
#         return self
# m = Money(100)
# print(m)
# # a = m
# a = Money(100)
# m %= 50
# print(m)
# m %= 100
# a %= 100
# print(f'{m}\t{a}')
# print(f'{id(a)}\t{id(m)}')
# #------------------
#=====================================
# # Задание
# # Перед вами несколько строк кода. Напишите что выведет программа, не запуская код. У вас 3 минуты.
# class MyClass:
#     def __init__(self, data):
#         self.data = data               
#     def __and__(self, other):
#         return MyClass(self.data + other.data)
#     def __str__(self):
#         return str(self.data)
# a = MyClass((1, 2, 3, 4, 5))
# b = MyClass((2, 4, 6, 8, 10))
# print(a & b)              # "1, 2, 3, 4, 5, 2, 4, 6, 8, 10" 
# """
# (1, 2, 3, 4, 5, 2, 4, 6, 8, 10)    # сложение кортежей
# """
#==========================

# 8. Сравнение экземпляров класса

# Числа сравниваются по значению, строки посимвольно. Но при желании можно сравнивать любые объекты Python реализовав перечисленные ниже дандер методы.
# ● __eq__ - равно, ==
# ● __ne__ - не равно, !=
# ● __gt__ - больше, >
# ● __ge__ - не больше, меньше или равно, <=
# ● __lt__ - меньше, <
# ● __le__ - не меньше, больше или равно, >=
# Перечисленные методы попарно противоположны. Обратите внимание на приставку не в списке. Реализовав один из пары, второй Python попытается получить инвертируя значение. Не истина — это ложь, а не ложь — это истина.
# При реализации метода обычно принято возвращать True или False. Если возвращается другое значение в конструкциях вида if x == y:, Python применит функцию bool() к результату для получения True или False.
#-------------
# Сравнение на идентичность, __eq__

# True if id(self) == id(other) else False

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# print(one == two)            # True
# print(one == three)          # False
# """
# True
# False
# """
#------------------
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#     def __eq__(self, other):
#         first = sorted((self.a, self.b, self.c))         # сортируем... 
#         second = sorted((other.a, other.b, other.c))     # ...списки сторон треугольника
#         return first == second
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two   = }')
# print(f'{one == three = }')
# print(f'{one == four  = }')
# print(f'{one != one   = }')
"""
one == two   = True
one == three = True
one == four  = True
one != one   = False
"""
#----------
# # Сравнение на больше и меньше
# # Формула Герона
# #     полупериметр p = (a + b + c) * 0.5
# #     площадь треугольника S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

# from math import sqrt
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#     def __repr__(self):
#         return f'Triangle({self.a}, {self.b}, {self.c})'
#     # def __eq__(self, other):
#     #     first = sorted((self.a, self.b, self.c))
#     #     second = sorted((other.a, other.b, other.c))
#     #     return first == second
#     def area(self):
#         p = (self.a + self.b + self.c) / 2
#         _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#         return _area
#     def __lt__(self, other):
#         return self.area() < other.area()
# one = Triangle(3, 4, 5)
# two = Triangle(5, 5, 5)
# print(f'{one} имеет площадь {one.area():.3f} у.е.²')
# print(f'{two} имеет площадь {two.area():.3f} у.е.²')
# print(f'{one > two  = }\n{one < two  = }')
# data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)]
# result = sorted(data)       # метов sorted - по умолчанию  __lt__
# print(result)
# print(', '.join(f'{item.area():.3f}' for item in result))

# # --
# # Неизменяемые экземпляры, хеширование дандер __hash__

# # triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
# # print(triangle_set)
# """
# TypeError: unhashable type: 'Triangle'
# """
# # закомментируем функцию сравнения
# ## def __eq__(self, other):
# #     first = sorted((self.a, self.b, self.c))
# #     second = sorted((other.a, other.b, other.c))
# #     return first == second
# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
# print(triangle_set)
# print(', '.join(f'{hash(item)}' for item in triangle_set))
# """
# Треугольник со сторонами: 3, 4, 5 имеет площадь 6.000 у.е.²
# Треугольник со сторонами: 5, 5, 5 имеет площадь 10.825 у.е.²
# one > two  = False
# one < two  = True
# [Triangle(3, 5, 3), Triangle(6, 2, 5), Triangle(3, 4, 5), Triangle(4, 4, 4)]
# 4.146, 4.684, 6.000, 6.928
# {Triangle(3, 4, 5), Triangle(3, 5, 3), Triangle(4, 4, 4), Triangle(6, 2, 5)}
# 2483312, 2483330, 2483324, 2483318
# """
# # Экземпляры треугольника стали хэшируемыми. Правило следующее.
# # ● нет __eq__, нет __hash__ - неизменяемый объект. Python сам реализует оба дандера
# # ● есть __eq__, нет __hash__ - изменяемый объект. Python устанавливает __hash__ = None
# # ● есть __eq__, есть __hash__ - неизменяемый объект реализованный разработчиком
# # ● нет __eq__, есть __hash__ - запрещённая комбинация! Разработчик допустил ошибку
# # Если вы хотите явно отключить поддержку хэширования, в определение класса добавляется строка __hash__ = None
#     # class Triangle:
#     # __hash__ = None
#     # ...
# # ------------
# Простейшая реализация хэша

# from math import sqrt
# class Triangle:
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
#     def __repr__(self):
#         return f'Triangle({self._a}, {self._b}, {self._c})'
#     def __eq__(self, other):
#         first = sorted((self._a, self._b, self._c))
#         second = sorted((other._a, other._b, other._c))
#         return first == second
#     def area(self):
#         p = (self._a + self._b + self._c) / 2
#         _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
#         return _area
#     def __lt__(self, other):
#         return self.area() < other.area()
#     def __hash__(self):
#         return hash((self._a, self._b, self._c))
# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
# print(triangle_set)
# print(', '.join(f'{hash(item)}' for item in triangle_set))
#===================================
# # Задание
# # Перед вами несколько строк кода. Напишите что выведет программа, не запуская код. У вас 3 минуты.
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.c = a + b
#     def __str__(self):
#         return f'MyClass(a={self.a}, b={self.b}, c={self.c})'
#     def __eq__(self, other):
#         return (sum((self.a, self.b)) - self.c) == (sum((other.a, other.b)) - other.c)   # 0 == 0 True
# x = MyClass(42, 2)   # True
# y = MyClass(73, 3)   # True
# print(x == y)  # True
# """
# True
# """

#============================
# # 9. Обработка атрибутов(четыре дандер метода)
# # a) Получение значения атрибута, __getattribute__. вызывается при любой попытке обращения к атрибутам экземпляра.
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)  
#         """Строка return object.__getattribute__(self, item) является обязательной. Без неё может возникнуть ошибка переполнения стека."""
# a = Vector(2, 4)
# #print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')
# #-----------------------------------------
# # Присвоение атрибуту значения, __setattr__ . срабатывает каждый раз, когда в коде есть операция
# # присвоения. Слева от знака равно экземпляр со свойством - key, справа значение - value.
# # Дандер __setattr__ запрещает присваивать значение свойству . Как и в случае с
# # __getattribute__ важная последняя строка.

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
# a = Vector(2, 4)
# print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')
# a.z = 73 # AttributeError: У нас вектор на плоскости, а не в пространстве
# a.x = 3
# print(f'{a = }')
# ------------
"""
# Обращение к несуществующему атрибуту, __getattr__
# """
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#     def __getattr__(self, item):
#         return None
# a = Vector(2, 4)
# print(a.z) # None
# print(f'{a = }')
#--------------------------------
# Удаление атрибута, __delattr__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)
    def __getattr__(self, item):
        return None
    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)
a = Vector(2, 4)
a.s = 73
print(f'{a = }, {a.s = }')
del a.x
del a.s
print(f'{a = }, {a.s = }')