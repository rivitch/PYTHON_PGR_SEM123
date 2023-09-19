# -*- coding: utf-8 -*-
# Модули

# import sys, _abc,  math  # импорт модуля в проект
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

# исправление ошибок при совпадении имен фаайла с именем модуля (05:50)
# пример - имее свой файл random.py

def randint(*args):
    return '"Error"'

# соседний файл task_import_02.py
import random

print(random.randint(1, 6))
