# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 

from random import randint

list_animal = ['Fish', 'Tiger', "Eagle"]
for key, value in enumerate(list_animal):
    print(key, value)
    pass

class AnimalFactory:
    def create_animal(self, animal_type, **kwargs):
        if animal_type == "Fish":
            return Fish(**kwargs)
        elif animal_type == "Tiger":
            return Tiger(**kwargs)
        elif animal_type == "Eagle":
            return Eagle(**kwargs)
        else:
            raise ValueError(f"Unsupported animal type: {animal_type}")

class Fish:
    def __init__(self, **kwargs):  # инициализация для класса Fish
        pass

class Tiger:
    def __init__(self, **kwargs):  # инициализация для класса Tiger
        pass

class Eagle:
    def __init__(self, **kwargs):  # инициализация для класса Eagle
        pass

factory = AnimalFactory()
animal = factory.create_animal("Tiger", name="Whiskers", age=3)
# y = map(str, animal)
# print(y)
for pet in animal.__str__:#list(animal):
    print(pet)

#==========================
# class Animal:
#     def __init__(self, name, age):  #, spec = None
#         self.name = name
#         self.age = age
#         #self.spec = spec
#     def get_spec(self):
#         return self.spec #self.name, self.age, 
#     pass

# class Dog(Animal):
#     def __init__(self, name, age, spec):
#         super().__init__(name, age)
#         self.spec = spec

# class Cat(Animal):
#     def __init__(self, name, age, spec):
#         super().__init__(name, age)
#         self.spec = spec

# class Fish(Animal):
#     def __init__(self, name, age, spec):
#         super().__init__(name, age)
#         self.spec = spec

# class Factory(Animal):
#     def __init__(self, name):#, age, spec
#         # super().__init__(name)
#         self.spec = spec
    

# name, age, spec, *_ = input().split()
# a = Factory(Dog(name, age, spec))
# print(a.get_spec())
