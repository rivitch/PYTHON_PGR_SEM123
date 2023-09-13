# -*- coding: utf-8 -*-
# Семинар 4, ДЗ 2.
# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если 
# ключ не хешируем, используйте его строковое представление.

def F_inverse(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        try:
            new_dict[value] = key
        except:
            new_dict[str(value)] = key       
    return new_dict       
print(F_inverse(a=7, b="qwe", c=3.14))