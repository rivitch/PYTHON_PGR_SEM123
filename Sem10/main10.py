import math

# # Создайте класс окружность. 📌
# # Класс должен принимать радиус окружности при создании экземпляра. 
# # У класса должно быть два метода, возвращающие длину окружности и её площадь.


# pi = 3.14

# class Circle: 
#     def __init__(self, r):
#         self.r = r
#     def len_circle(self):
#         return 2*pi*self.r
#     def s_circle(self):
#         return pi*(self.r**2) 
    
# r = float(input()) 
# a = Circle(r)
# #b = Circle(r)
# print(f'Длина окружности {a.len_circle()}\nПлощадь круга {a.s_circle()}')

# ------------------------
# # 2.СОЗДАЙТЕ КЛАСС ПРЯМОУГОЛЬНИК. 
# # КЛАСС ДОЛЖЕН ПРИНИМАТЬ ДЛИНУ И ШИРИНУ ПРИ СОЗДАНИИ ЭКЗЕМПЛЯРА. 
# # У КЛАССА ДОЛЖНО БЫТЬ ДВА МЕТОДА, ВОЗВРАЩАЮЩИЕ ПЕРИМЕТР И ПЛОЩАДЬ. 
# # ЕСЛИ ПРИ СОЗДАНИИ ЭКЗЕМПЛЯРА ПЕРЕДАЁТСЯ ТОЛЬКО ОДНА СТОРОНА, СЧИТАЕМ ЧТО У НАС КВАДРАТ.

# class Rectangle: 

#     def __init__(self, side_a, side_b=None):
#         self.side_a = side_a
#         self.side_b = side_b if side_b else side_a

#     def perimeter(self):
#         return (self.side_a + self.side_b) * 2
#     def area(self):
#         return self.side_a * self.side_b

# side_1, side_2, *_ = map(float, (input().split()))
# a = Rectangle(side_1, side_2)
# print(f'ПЕРИМЕТР {a.perimeter()}\nПлощадь {a.area()}')

# ======================
# # 3.Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# # У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
# # Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

# class InfoMan:
#     def __init__(self, family, first_name, second_name, age):
#         self.family = family
#         self.first_name = first_name
#         self.second_name = second_name
#         self.__age = age
#         #self.side_b = side_b if side_b else side_a
#     def birthday(self):
#         return int(age) + 1
#     def full_name(self):
#         return family + " " +first_name + " " + second_name
#     def show_age(self):
#         return self.__age
#     pass

# family, first_name, second_name, age, *_ = input().split()
# a = InfoMan(family, first_name, second_name, age)
# #b = InfoMan(age)
# #print(f'Полное имя {a.full_name()}\nЧерез год будет {a.birthday()}\nТекущий возраст {a.__init__.self._age}')
# print(f'Полное имя {a.full_name()}')
# print(f'Через год будет {a.birthday()}')
# print(f'Текущий возраст {a.show_age()}')
# print(f'Текущий возраст {a._InfoMan__age}')
# #print(f'Текущий возраст {a.birthday.self._age}') #????????????????

#==================
# 4.Создайте класс Сотрудник. 
# Воспользуйтесь классом человека из прошлого задания. 
# У сотрудника должен быть: ○ шестизначный идентификационный номер, уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь

# from random import randint

# class Coworcer(InfoMan):
#     def __init__(self, family, first_name, second_name, age):
#         self.family = family
#         self.first_name = first_name
#         self.second_name = second_name
#         self.__age = age    
#     pass

# -----------------------

# 5. Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.




#----------------------------
# 6. Доработайте задачу 5. 
# Вынесите общие свойства и методы классов в класс Животное. 
# Остальные классы наследуйте от него. 
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, age, spec = None):
        self.name = name
        self.age = age
        self.spec = spec
    def get_spec(self):
        return self.spec
    #pass
    pass

class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age, spec)
        self.spec = spec

class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        
class Factory(Dog, Cat, Fish):
    def __init__(self, name, age, spec):
        super().__init__(name, age, spec)
        self.spec = spec
        name, age, spec, *_ = input().split()
        a = Animal(name, age, spec)
        return a
    pass      

# name, age, spec, *_ = input().split()
# a = Animal(name, age, spec)
# family, first_name, second_name, age, *_ = input().split()
# a = InfoMan(family, first_name, second_name, age)
# #b = InfoMan(age)
#print(f'Полное имя {a.full_name()}\nЧерез год будет {a.birthday()}\nТекущий возраст {a.__init__.self._age}')
#print(f'Полное имя {a.Dog()}')
# print(f'Через год будет {a.birthday()}')
# print(f'Текущий возраст {a.show_age()}')
# print(f'Текущий возраст {a._InfoMan__age}')