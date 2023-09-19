# -*- coding: utf-8 -*-
# Модули

# import sys, _abc,  math  # импорт модуля в проект
# import math                # по PEP8 каждый модуль прописывается в отдельной строке  
# import_abc
# # пустая строка
# print(sys, _abc)
# print(sys.builtin_module_names)    #список встроенных модулей
# print(*sys.path, sep = '\n')   #поиск модуля по директориям
# print(*_abc.path, sep = '\n')
# #print(*math.path, sep = '\n')

# Вывод
# <module 'sys' (built-in)>    # Модуль встроен в Python стандартную библиотеку
# ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')   # Список встроенных модулей
# i:\GB\TASKS\PYTHON_PGR_SEM123\Sem6        Директория проекта откуда начинаеся поиск библиотеки 
# I:\GB\PROGRAMMS\Python38\python38.zip     
# I:\GB\PROGRAMMS\Python38\DLLs
# I:\GB\PROGRAMMS\Python38\lib
# I:\GB\PROGRAMMS\Python38
# I:\GB\TASKS\PYTHON_PGR_SEM123\.virt
# I:\GB\TASKS\PYTHON_PGR_SEM123\.virt\lib\site-packages

# Если модули не найдены выдаст ошибку
# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem6/Lec6.py", line 9, in <module>
#     print(*_abc.path, sep = '\n')
# AttributeError: module '_abc' has no attribute 'path'

#  -----------------------------------

# # исправление ошибок при совпадении имен фаайла с именем модуля (05:50)
# # пример - имее свой файл random.py

# def randint(*args):
#     return '"Что-то тут не так"'

# # соседний файл task_import_02.py
# import random

# print(random.randint(1, 6))  # при запуске получаем "Что-то тут не так"
# # выход - добавление к имени совпадающего с именем модуля символа "_"
# --------------------------------

# # Использование from и as

# from sys import builtin_module_names, path

# print(builtin_module_names)
# print(*path, sep = '\n')
# #---
# import random  as rnd
# from sys import builtin_module_names  as bmn, path as p

# print(bmn)
# print(*p, sep = '\n')
# print(rnd.randint(1, 6))
# print(builtin_module_names, '\n')
# print(*path, '\n')
# print(path, '\n')       
# print(sys.path)
# #  Вывод
# Traceback (most recent call last):
#   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem6/Lec6.py", line 62, in <module>
#     print(sys.path)
# NameError: name 'sys' is not defined

# ---------------------------------------------------

# # Плохой import * (импорт звёздочка)  (11:20)
# # from имя_модуля import *

# # super_module.py

# from sys import randint

# SIZE = 100
# _secret = 'qwer'             # 1 подчеркивание впереди переменной - защищенная переменная
# __top_secret = 'qwerty123'   # 2 подчеркивания впереди переменной - приватная переменная

# def func(a: int, b: int) -> str:
#     z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
#     return z

# result = func(1, 6)

# # task_import_06.py

# from super_module import *

# SIZE = 49.5
# print(f'{SIZE = }\n{result = }')
# print(f'{z = }')
# print(f'{_secret = }')
# print(f'{func(100, 200) = }\n{randint(10, 20) = }')

# def func(a: int, b: int) -> int:
#     return a + b


# print(f'{func(100, 200) = }')

# # # Вывод
# # Traceback (most recent call last):
# #   File "i:/GB/TASKS/PYTHON_PGR_SEM123/Sem6/task_import_06.py", line 1, in <module>
# #     from super_module import *
# #   File "i:\GB\TASKS\PYTHON_PGR_SEM123\Sem6\super_module.py", line 1, in <module>
# #     from sys import randint
# # ImportError: cannot import name 'randint' from 'sys' (unknown location)

# ---------------------------------------

# # Файл base_math.py
# """Four basic mathematical operations.
# Addition, subtraction, multiplication and division as functions.
# """
# _START_SUM = 0
# _START_MULT = 1
# _BEGINNING = 0
# _CONTINUATION = 1

# def add(*args):
#     res = _START_SUM
#     for item in args:
#         res += item
#     return res

# def sub(*args):
#     res = args[_BEGINNING]
#     for item in args[_CONTINUATION:]:
#         res -= item
#     return res

# def mul(*args):
#     res = _START_MULT
#     for item in args:
#         res *= item
#     return res

# def div(*args):
#     res = args[_BEGINNING]
#     for item in args[_CONTINUATION:]:
#         res /= item
#     return res

# print(f'{add(2, 4) = }')
# print(f'{add(2, 4, 6, 8) = }')
# print(f'{sub(10, 2) = }')
# print(f'{mul(2, 2, 2, 2, 2) = }')
# print(f'{div(-100, 5, -2) = }')

# ----------------------------
# (34:00)
# # импорт модуля other_module в другой модуль того же пакета можно осуществить
# через относительный импорт:
# from . import other_module
# А если модулю надо выйти из своего пакета в пакет верхнего уровня, используют
# вторую точку:
# from .. import other_module
# Или так
# from ..other_package import other_module

# ----


