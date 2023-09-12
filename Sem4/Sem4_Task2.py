# -*- coding: utf-8 -*-
# Семинар 4, ДЗ 2.
# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если 
# ключ не хешируем, используйте его строковое представление.

# from random import randint
# from pprint import pp
# _tuple = (1, 2, 3)
# _list = 
#_valKwargs = [1=12,3=35,2=1,5=15,4=0]
a = 1
b = 2
x = id(a)
b = id{b}
_dict1 = {}
def F_my(**kwargs):
    for key, value in kwargs.items():
        #_dict1.append(value: key)
        _dict1.update(kwargs.items())
        print(_dict1)
    return _dict1
    pass
print(F_my(_valKwargs))