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

# Методы upper, lower, title, capitalize
text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())  #  верхний  регистр
print(text.lower())  #  нижний регистр
print(text.title())  #  кАЖДОЕ СЛОВО С ЗАГЛАВНОЙ   
print(text.capitalize()) # фраза с заглавной