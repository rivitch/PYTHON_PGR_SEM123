# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 


class Animal:
    def __init__(self, name, age):  #, spec = None
        self.name = name
        self.age = age
        #self.spec = spec
    def get_spec(self):
        return self.spec
    pass

class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Factory(Animal):
    def __init__(self, name):#, age, spec
        # super().__init__(name)
        self.spec = spec


name, age, spec, *_ = input().split()
a = Factory(Fish(name, age, spec))
print(a.get_spec())
