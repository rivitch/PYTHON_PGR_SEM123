"""#Обмен значения переменных
a=42
b=73
#c = tuple(a,b) # не работает
a,b = tuple((a,b)) # создание кортежа из элементов
#a, b = dict((a,b))не работает
#a , b = c      # не работает
a,b = b,a    # <<<<<<<<<<<<<<<<<
print(f'{a = }\t{b = }')   # a = 73  b = 42
print(tuple((b,a)))
#print(dict((a,b)))"""

###---------
# 2 Распаковка коллекции
"""a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}')
# Как вы помните функция input возвращает строку str. Указав не одну переменную, а
# три мы распаковываем строку из 3-х символов в три отдельные переменные.
a, b, c = ("один", "два", "три",)   # кортеж
print(f'{a=} {b=} {c=}')            # доступен поэлементно
# Аналогичным образом можно распаковать кортеж из трёх элементов в три
# переменные. Со списком list, множеством set и прочими коллекциями будет
# работать аналогично.
a, b, c = {"один", "два", "три", "четыре", "пять"}
#print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack(expected 3)"""

###-----------------------
# Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
"""data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",
]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
#Элементы коллекции попадают в переменные в зависимости от того, какая из переменных отмечена звёздочкой.Звёздочкой можно отметить только одну переменную из перечня.

# Если нам нужна часть данных в переменных, а упакованный список в дальнейших
# расчётах не участвует, в качестве переменной используют подчеркивание.
link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')   #вырезали из строки все ненужное
print(link)  # сама строка не изменилась
print(prefix, suffix)

#Распаковка со звёздочкой
#Ещё один способ применения звёздочки — распаковка элементов коллекции.
#Длинный вариант вывода элементов последовательности в одну строку с разделителем табуляцией:
data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')
#И аналогичная операция в одну строку с распаковкой:
data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')"""

#------------------------
#Множественное присваивание
"""a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')    #  a=42 b=0 c=0
# Подобная запись допустима только с неизменяемыми типами данных tuple, string, frozenset, dict.keys. 
# В противном случае изменение одной переменной приведёт к изменению и других.
a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')     # a={1, 2, 3, 42} b={1, 2, 3, 42} c={1, 2, 3, 42}

a = {1, 2, 3}
b = {1, 2, 3}
c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')     # a={1, 2, 3, 42} b={1, 2, 3} c={1, 2, 3}

# вариант множественного присваивания похож на обмен переменных
a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')
# Число элементов в левой части должно совпадать с числом элементов справа от равно.
# А если в левой части указать лишь одну переменную, получим кортеж.
t = 1, 2, 3
print(f'{t=}, {type(t)}')
###-----------------------
# Множественное сравнение
a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')
if a < b < c:
    print('b больше a и меньше c')"""
###------------
#  Плохие однострочники
"""a = 12; b = 42; c = 73      # Перечислили несколько операций присваивания через точку с запятой в одной строке.
if a < b < c: b = None; print('Ужасный код') # не перешли на новую строку с отступами после двоеточия.запись нескольких строк кода в одну через точку с запятой
###############
#Задание
data = {10, 9, 8, 1, 6, 3}
a, b, c, *d, e = data
print(a, b, c, d, e)
# 10, 9, 8, [1, 6], 3   неверно
# внутри множества алг хеширования. чем больше число - тем больше хеш. 1, 3, 6, [8, 9], 10"""
#==============================================================
## 2. Итераторы
# итераторы чаще всего возвращают коллекции. Т.е. коллекция хранит все данные и тратит на хранение память.
#Если коллекцию можно передать в цикл for in для последовательного перебора элементов, значит коллекция
#итерируемая.Списки, строки, кортежи возвращают элементы слева направо, от нулевого индекса к последнему. Множества возвращают элементы в случайном порядке. НО - Хэш функция определяет в какое место множества будет помещён элемент и возвращает их в порядке возрастания хеша.
# словари поддерживают сразу три интерфейса итерации: по ключам - метод keys, по значениям - метод values и по парам ключ-значение - метод items. 
# --------------------------------------
#Функция iter имеет формат iter(object[, sentinel]). object является обязательным аргументом.

# a = 42
# iter(a) # TypeError: 'int' object is not iterable

#итератор списка
"""data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)    # <list_iterator object at 0x0000000001E3A940

# переменная list_iter указывает на <list_iterator object at 0x0000025383D29400>, т.е.
# объект итератор списка (место в памяти, где список data). Для кортежа функция iter вернёт tuple_iterator, для
# множеств set_iterator, а например для dict.items() вернётся dict_itemiterator.
# выход - распаковать итератор через звёздочку.
data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter) # итератор является одноразовым объектом. Получив все элементы коллекции один раз он перестаёт работать. Для повторного извлечения элементов необходимо создать новый итератор.

# Второй параметр функции iter — sentinel передают для вызываемых
# объектов-итераторов. Параметр указывает в какой момент должна быть завершена
# итерация, при совпадении возвращаемого значения со значением sentinel.
data = [2, 4, 6, 8]
list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable Список не является функцией, его нельзя вызвать.
# Один из вариантов работы функции iter с двумя параметрами — чтение бинарного файла блоками фиксированного размера до тех пор, пока не будет достигнут конец файла. (27:40) - проверить

import functools
f = open('mydata.bin', 'rb')      # Открыли бинарный файл на чтение байт.  
for block in iter(functools.partial(f.read, 16), b''): # Чтение прекратиться после считывание пустого байта b’’ , окончания файла.В цикле считываем блоки по 16 байт и 
print(block)                                             #выводим их на печать.
f.close()                #После этого выходим из цикла и закрываем файл."""

# --------------------------
#Функция next имеет формат next(iterator[, default]). На вход функция принимает итератор, который вернула функция iter. Каждый вызов функции возвращает очередной элемент итератора.
"""data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter)) # StopIteration
#При завершении элементов выбрасывается исключение StopIteration. цикл обрабатывает его как сигнал для завершения итерации и перехода к следующему блоку кода. Исключение не останавливает программу.
#Второй параметр функции next нужен для возврата значения по умолчанию вместо выброса исключения StopIteration
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
###+++++++++++++++++++++++++
# Промежуточный итог. Любая коллекция в Python поддерживает интерфейс
# итерации, т.е. перебор элементов в цикле for in. Для этого она возвращает итератор"""
###+++++++++++++++++++++++++
# Задание
# Перед вами несколько строк кода Напишите что выведет каждая из строк, не
# запуская код. У вас 3 минуты. (34:30) - темный лес, повторить
"""data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items()) 
print(x)     # ("один": 1)
y = next(x)
print(y)     # ("два": 2)
z = next(iter(y))
print(z)     # ссылка на объект ("два": 2)
# <dict_itemiterator object at 0x0000000001E51F40>
# ('один', 1)
# один"""

##============================================
#3. Генераторы (36Ж30)
# Генераторы не хранят данные в памяти, а вычисляют их по мере необходимости, чтобы вернуть очередное значение.
# На асимптотическую сложность генератора влияют только количество циклов.
"""a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')
#Принт
# a=range(0, 10, 2), type(a)=<class 'range'>, a.__sizeof__()=48, 5
# b=range(-1000000, 1000000, 2), type(b)=<class 'range'>, b.__sizeof__()=48, 1000000
#Генератор a на пять значений и генератор b на 1 млн. значений занимают одинаковое место в памяти."""


#--------------
"""my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)
# Для создания генераторного выражения используют круглые скобки, внутри которых прописывается логика выражения. В нашем примере циклический перебор целых чисел от 97 до 122 и возврат символов из таблицы ASCII с соответствующими кодами.

При работе с генераторами стоит помнить, что для каждого витка внешнего цикла
внутренний перебирает все элементы от начала до конца. Например:"""
"""x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
#print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

# разворот     обратная писанина
mult_1 = []
for i in x:
    if i % 2 != 0:
        for j in y:
            if j != 1:
                mult_1.append(str(i + j))
res_1 = list(map(int, mult_1))
print(f'{len(res_1)=}\n{res_1}')

#PEP-8! Ограничение в 80 (120) символов на строку касается и генераторов. Если
# ваш код выходит за границу, попробуйте его упростить. Если упрощение
# невозможно, стоит перейти от однострочного генераторного выражения к функции
# генератору. Их мы рассмотрим далее на уроке.
# Аналогичные ограничения касаются и рассматриваемых далее генераторов
# списков, множеств и словарей."""
# ----------------------------------

#List comprehensions
#  если генераторное выражение записать не в круглых скобках, а в
# квадратных Получим list comprehensions. Другие названия: list comp, генератор
# списков, списковое включение. И нет, это не генераторное выражение. Генератор
# списков полностью формирует список с элементами до его присваивания переменной слева от знака равно.
# my_listcomp = [chr(i) for i in range(97, 123)]
# print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
# for char in my_listcomp:
#     print(char)

# все чётные числа из исходного списка и складываем их в результирующий.
#Длинный код:
"""data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')
#Аналогичное решение, но с использованием синтаксического сахара listcomp:
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')
# 1. Не создаём пустой список в начале.
# 2. Не пишем двоеточия после цикла и логической проверки.
# 3. Исключаем метод append.
# Итого вместо 4 строк кода получаем одну."""

####--------------------
# Если на выходе нужен готовый список, оптимальным будет следующий код:  
"""x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]     # [квадратные скобки]
print(f'{len(res)=}\n{res}')
# А если нам не нужны все элементы разом. Например мы в дальнейшем хотим
# перебирать значения по одному в цикле. В этом случае подойдет генераторное
# выражение без преобразования в список.
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)    # [круглые скобки]
for item in mult:
    print(f'{item = }')"""
# --------------
#Set comprehensions - генерация множеств .Для множеств используются фигурные скобки.
"""my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

# порядок элементов внутри множества может не совпадать с порядком добавления элементов.
# множество хранит только уникальные значения
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}') 
#6 дублирующих элементов не были добавлены в множество, но время на их обработку было затрачено. Асимптотика не улучшилась."""
# -------
# Dict comprehensions  - генерация словаря.Для словаря используются фигурные скобки. Отличия в двоеточии между переменными перед for
"""my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
# Запись похожа на создание множества, но в качестве выражения для добавления
# указываются две переменные через двоеточие: key: value.ключи словаря должны быть объектами неизменяемого типа."""

# -------------------
#Задание
# Перед вами несколько строк кода. Напишите что по вашему мнению выведет print,
# не запуская код. У вас 3 минуты.
data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}    # {6:None, 8:None, 10:None, 12:None}   ХЭШ!!!
res2 = (item for item in data if item > 4)          # (6, 8, 10 ,12)
res3 = [[item] for item in data if item > 4]        #  [[6], [8], [10], [12]]
print(res1, res2, res3)
#   {None: 12} <generator object <genexpr> at 0x00000000025A6F90> [[6], [8], [10], [12]]
# ---------
#
#=========================================
# 4. Создание функции генератора





# 
# 
# 
# 
#     
