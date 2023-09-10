# # Создание списков
# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# print(list_2)
# list_3 = []       # работает быстрее
# list_4 = [3.14, True, "Hello world!"]
# list_5 = list(list_2)
# print(list_5)

# # Метод append    : добавляет элемент в конец списка. не копирует сам себя
# print("Метод append")
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list)
# my_list.append(b)
# print(my_list)
# my_list.append(c)
# print(my_list)
# my_list.append(my_list)  # добавили в список сам себя.
# print(my_list,"\n")           # Вывод: [None, 42, 'Hello world!', [1, 3, 5, 7], [...]]

# #Метод extend  -  добавляет элемент в конец списка. не работает с int. (проверить с bool)
# print("\nМетод extend\n")
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# # my_list.extend(a) # TypeError: 'int' object is not iterable
# # print(my_list)
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list)
# print(my_list)

# # Метод pop позволяет удалить элемент списка.
# print("\nМетод pop")
# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)
# print(my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# #err = my_list.pop(10) # IndexError: pop index out of range
# #print(err, my_list)
# print(spam)

# # Метод count подсчитывает вхождение элемента в список.
# print("\nМетод count")
# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.count(2)
# print(spam)
# eggs = my_list.count(3)
# print(eggs)

# # Метод index возвращает индекс переданного объекта внутри списка.Метод работает до первого вхождения
# print("\nМетод index")
# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.index(4)
# print(spam) # возвращается индекс первой встречи.
# eggs = my_list.index(4, spam + 1, 90) # два дополнительных аргумента: индекс start и индекс stop.
# print(eggs)
# #err = my_list.index(3) # ValueError: 3 is not in list

# # Метод insert принимает на вход два аргумента — индекс для вставки и объект вставки. Метод добавляет элемент после индекса.
# print("\nМетод insert")
# my_list = [2, 4, 6, 8, 10, 12]
# my_list.insert(2, 555)
# print(my_list)
# my_list.insert(-2, 13)
# print(my_list)
# my_list.insert(42, 73) # my_list.append(73)  # когда индекс оказывается больше, чем количество элементов списка,объект добавляется в конец.
# print(my_list)

# # Метод remove принимает на вход объект, производит его поиск в списке и удаляет в случае нахождения.Если удаляемый элемент встречается в списке несколько раз, удаляется только один элемент — самый левый. А если удаляемый элемент отсутствует в списке, будет вызвана ошибка ValueError.
# print("\nМетод remove")
# my_list = [2, 4, 6, 8, 10, 12, 6]
# my_list.remove(6)
# print(my_list)
# # my_list.remove(3) # ValueError: list.remove(x): x not in list
# # print(my_list)

# # Функция sorted принимает на вход любую коллекцию по которой можно итерироваться и всегда возвращает отсортированный СПИСОК.
# print("\nФункция sorted")
# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True) # True - сортировка по убыванию.
# print(my_list, rev_list, sep='\n')

# # Метод sort осуществляет сортировку элементов списка без создания копии, память не тратим
# print("\nМетод sort")
# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# # Функция reversed() принимает на вход последовательность, возвращает  объект итератор с обратным порядком элементов. затратна по времени и по памяти.
# print("\nФункция reversed")
# my_list = [4, 8, 2, 9, 1, 7, 2]
# # print(my_list)
# res = reversed(my_list)
# # print(res)
# print(type(res), res)
# rev_list = list(reversed(my_list))
# print(rev_list)
# # res_1 = reversed(rev_list)
# # print(res_1)
# for item in reversed(my_list):
#     print(item)

# # Метод reverse() Метод разворачивает список на месте не создавая копии.
# print("\nМетод reverse")
# my_list = [4, 8, 2, 9, 1, 7, 2]
# # print(my_list)
# my_list.reverse()
# print(my_list)

# # Срезы Используем квадратные скобки, можно делать частичные копии списка - срезы.
# # list[start:stop:step]
# # start указывает на первый индекс, который включается в срез. При отсутствии значения start равен нулю, началу списка.
# # stop указывает на последний индекс, который не включается в срез. При отсутствии значения stop равен последнему элементу списка и включает его в срез.
# # step — шаг движения от star до stop. По умолчанию step равен единице, все элементы по порядку.
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list)
# print(my_list[2:7:2])
# print(my_list[:7:2])
# print(my_list[2::2])
# print(my_list[2:7:])
# print(my_list[8:3:-1])
# print(my_list[3::])
# print(my_list[:7:])

# # Метод copy создаёт поверхностную копию списка. создает копию верхнего уровня.
# # Плохой пример
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n') # оба списка изменились
# # хороший пример
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy()
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n') # изменился только первый список

# # функция copy.deepcopy()  для создания полной копии любой глубины вложенности используют функцию deepcopy из модуля copy.
# # # Плохой пример
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')   # оба списка изменились
# # # хороший пример
# import copy
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')

# # Функция len
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(len(my_list))
# print(len(matrix))
# print(len(matrix[1]))

# # Проверка
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:6:2])
# print(my_list.pop())
# print(my_list.extend([314, 42]))  # ?
# print(my_list.sort(reverse=False))# ?
# print(my_list)

# #Работа со строками
# text = 'Hello world!'
# print(text[6])
# print(text[3:7])

# # метод replace
# # Первый аргумент — подстрока, которую нужно заменить.
# # Второй аргумент — подстрока, на которую нужно заменить.
# # Третий аргумент — максимальное количество замен. Если его не указывать, будут заменены все совпадения.
# new_txt = text.replace('l', 'L', 2)
# print(text, new_txt, sep='\n')

# # Методы count, index для строк. новый метод ﬁnd 
# text = 'Hello world!'
# print(text.count('l'))
# print(text.index('l',0,11))
# print(text.find('l'))
# print(text.find('z'))

# # Форматирование строк
# # Методы %, format и f 
# name = 'Alex'
# age = 12
# text = 'Меня зовут %s и мне %d лет' % (name, age) # очень старые версии
# print(text)
# text = 'Меня зовут {} и мне {} лет'.format(name, age )# просто старые версии
# print(text)
# text = f'Меня зовут {name} и мне {age} лет'  # работает быстрее. начало с python 3.7
# print(text)
# print(f'{{Фигурные скобки}} и {{name}}') # Фигурные скобки

# # Уточнение формата
# # Существую различные способы уточнения способа вывода значения переменной.
# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}')
# data = [3254, 4364314532, 43465474, 2342, 462256, 1747, 1]
# for item in data:
#     print(f'{item:>10}') # :>10 — элементы списка выравниваются по правому краю и общей шириной вывода в 10 символов
#     print(item)
#     num = 2 * pi * item  
#     print(f'{num = :_}') # :_ — число разделяется символом подчёркивания для деления на блоки по 3 цифры.
# num = 2 * pi * data[6]
# print(f'{num = :_}')

# # Метод split  разбивает строку на отдельные элементы в соответствии с разделителем(по умолчнию пробел) и помещает результат в список.
# link = 'https://habr.com/ru/users/dzhoker1/posts/'
# urls = link.split('/') # взяли ссылку и разделили её на отдельные компоненты по символу “/”
# print(urls)
# a, b, c = input('Введите 3 числа через пробел: ').split() # метод не получил на вход аргументы и деление происходит по пробельным символам. Три переменные до знака равно примут по одному из переданных значений.
# print(c, b, a)
# # ошибки с пробелами и(или) ввод меньше или больше трёх чисел, получим ошибку: ValueError: too many values to unpack (expected 3) или ValueError: not enough values to unpack (expected 3, got 2)
# # Избежание.  использовать символ распаковки *_.
# a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()
# print(int(c) - int(b)+ int(a))

# # Метод join
# data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts']
# url = '/'.join(data)
# print(url)

# # Методы upper, lower, title, capitalize
# text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())  #  верхний  регистр
# print(text.lower())  #  нижний регистр
# print(text.title())  #  кАЖДОЕ СЛОВО С ЗАГЛАВНОЙ   
# print(text.capitalize()) # фраза с заглавной

# # Методы startswith и endswith. проверяет начинается ли строка с заданной подстроки. Метод возвращает истину или ложь.
# text = 'Однажды в студёную зимнюю пору'
# print(text.startswith('Однажды'))
# print(text.endswith('зимнюю', 0, -5)) # могут принимать параметры start и stop

# # Задание 
# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>25}')

# # Кортеж. 
# # 1. Пара круглых скобок создаёт пустой кортеж
# # 2. Один элемент с замыкающей запятой в скобках или без них создаёт кортеж с элементом
# # 3. Несколько элементов разделенных запятыми с замыкающей запятой или в круглых скобках
# # 4. Функция tuple(), которой передаётся любой итерируемый объект
# # Важно! Обратите внимание, что на самом деле кортеж образует запятая, а не круглые скобки. Круглые скобки необязательны, за исключением случая пустого кортежа или когда они необходимы, чтобы избежать синтаксической неоднозначности. Например, f(a, b, c) — это вызов функции с тремя аргументами. f((a, b, c)) — вызов функции с кортежем в качестве единственного аргумента.
# a = ()
# b1 = 1,
# b2 = (1,)
# c1 = 1, 2, 3,
# c2 = (1, 2, 3)
# d = tuple(range(3))
# print(a, b1, b2, c1, c2, d, sep='\n')

# # Задание
# my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
# # g_tuple= "text",2,
# print(my_tuple[2:6:2])
# print(my_tuple[-3])
# print(my_tuple.count(2))
# print(f'{my_tuple = }')
# print(my_tuple.index(2, 2))
# # print(type("text",))
# # print(type(g_tuple))

# # словарь
# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
# b = dict(one=42, two=3.14, ten='Hello world!')
# c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
# print(a == b == c)
# # добавление
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# print(my_dict)
# # Доступ к значению словаря через квадратные скобки []
# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict['two'])
# print(my_dict[TEN])
# #print(my_dict[1]) # KeyError: 1
# # Доступ через метод get
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.get('two'))
# print(my_dict.get('five'))
# print(my_dict.get('five', 5))
# print(my_dict.get('ten', 5))

# # Метод setdefault
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.setdefault('five')
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# new_spam = my_dict.setdefault('two')
# print(f'{new_spam=}\t{my_dict=}')
# new_eggs = my_dict.setdefault('one', 1_000)
# print(f'{new_eggs=}\t{my_dict=}')
# # new_eggs = my_dict.setdefault(7, 1_000)
# # print(f'{new_eggs=}\t{my_dict=}')

# # Метод keys возвращает объект-итератор dict_keys.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# # # Метод values
# # Метод values похож на keys, но возвращает значения в виде объекта итератора dict_values, а не ключи.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.values())
# for value in my_dict.values():
#     print(value)

# # Метод items
# # Если в цикле необходимо работать одновременно с ключами и значен парами,  используют метод items.
# # Метод возвращает объект итератор dict_items. Если создать цикл for с одной
# # переменной между for и in, получим кортеж из пар элементов — ключа и значения.
# # Две переменные в цикле: первая принимает ключ, а вторая значение.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.items())
# for tuple_data in my_dict.items():
#     print(tuple_data)
# for key, value in my_dict.items():
#     print(f'{key = } value before 100 - {100 - value}')

# # Метод popitem
# # Для удаления пары ключ значение из словаря используют метод popitem.
# # Так как словари сохраняют порядок добавления ключей, удаление происходит
# # справа налево, по методу LIFO. Элементы удаляются в обратном добавлению порядке.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.popitem()
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict=}')

# # Метод pop
# # Метод pop удаляет пару ключ-значение по переданному ключу.
# # Если указать несуществующий ключ, получим ошибку KeyError. 
# # В отличии от метода pop у списков list, dict.pop вызовет ошибку TypeError. 
# # Для удаление последнего элемента нужен метод popitem.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.pop('two')
# print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six') # KeyError: 'six'
# err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

# # Метод update
# # Для расширение словаря новыми значениями используют метод update.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# my_dict.update(dict(six=6))
# print(my_dict)
# my_dict.update(dict([('five', 5), ('two', 42)]))
# print(my_dict)
# # На вход метод получает другой словарь в любой из вариаций создания словаря.
# # Если передать существующий ключ, значение будет заменено новым.
# # Ещё один способ создать словари из нескольких других, который появился в новой версии Python — вертикальная черта.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# # new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)  # в   3.8.10   "|"  не работает
# print(new_dict)
# # При перезаписи совпадающих ключей приоритет отдаётся словарю, расположенному правее.

# # Задание
# # Перед вами словарь и несколько строк кода. Напишите что вернёт каждая из строк.
# # Попробуйте справится с заданием без запуска кода. У вас 3 минуты.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)

# # Множество — набор уникальных неиндексированных элементов. В Python есть два вида множеств: set —
# # изменяемое множество, frozenset — неизменяемое множество. Неизменяемое множество позволяет вычислять хеш и 
# # может использоваться там, где разрешён лишь хешированный тип данных, например в качестве ключа словаря.
# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# # not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'

# # Метод add
# # Метод add работает аналогично методу списка append, т.е. добавляет один элемент в коллекцию.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# # my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
# my_set.add((9, 10))
# print(my_set)
# # my_set.add(("9", "10"))
# # print(my_set)
# # my_set.add(("a", "b"))
# # print(my_set)
# # a=b=None
# # my_set.add((a, b))
# # print(my_set)

# # Метод  remove Для удаления элемента множества.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.remove(5)
# print(my_set)
# my_set.remove(10) # KeyError: 10 # При передаче несуществующего объекта получим ошибку KeyError.

# # Метод  discard
# # Метод discard работает аналогично remove—удаляет один элемент множества.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.discard(5)
# print(my_set)
# my_set.discard(10)  # В отличии от remove при попытке удалить несуществующий элемент discard не вызывает ошибку. При этом множество не изменяется.

# # Метод  intersection
# # Для получения пересечения множеств, т.е. множества с элементами, которые есть и в левом и в правам множестве используют метод intersection
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.intersection(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# # версия 3.8.10  позволяет получить пересечение множеств в следующей записи c использованием символа &
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set & other_set
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# # Метод  union Для объединения множеств.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
# # На выходе получаем множество уникальных элементов из левого и правого множеств. Более короткая запись объединения возможна при помощи вертикальной черты. работает в 3.8.10

# # Метод  difference удаляет из левого множества элементы правого.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set - other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
# # На выходе получаем множество элементов встречающихся только в левом множестве. Более короткая запись возможно при помощи знака минус. Вычитаем из левого элементы правого

# # Проверка на вхождение, in
# # Для проверки входит ли элемент в множество используют зарезервированное слово in.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# print(42 in my_set)
# # Внимание! Слово in позволяет сделать проверку на вхождение и в других
# # коллекциях. Входит ли объект в list, tuple, является ли подстрока частью строки
# # str, встречается ли ключ в словаре. Для list, tuple, str проверка на вхождение
# # работает за линейное время O(n). Для dict, set, frozenset проверка работает за
# # константное время O(1)

# #Задание
# # Перед вами множество и несколько строк кода. Напишите что вернёт каждая из
# # строк. Попробуйте справится с заданием без запуска кода. У вас 3 минуты.
# my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
# print(len(my_set))  # 7
# print(my_set - {1, 2, 3})  # 4,5,6,7
# print(my_set.union({2, 4, 6, 8})) # 1,2,4,5,6,7,8  - (3)
# print(my_set & {2, 4, 6, 8}) # 2,4,6
# print(my_set.discard(10)) # 1,2,3,4,5,6,7  - (AttributeError: 'frozenset' object has no attribute 'discard')

# # Классы bytes и bytearray
# text_en = 'Hello world!'
# res = text_en.encode('utf-8')
# print(res, type(res))
# text_ru = 'Привет, мир!'
# res = text_ru.encode('utf-8')
# print(res, type(res))
# x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
# y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
# print(f'{x = }\n{y = }')