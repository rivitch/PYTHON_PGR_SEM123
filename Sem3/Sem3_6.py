# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

_inp = "Cтроку вводит пользователь текста"
print(_inp)
list_1 = _inp.split()
len_max = max(list_1, key=len)
print(len_max)
list_1.sort()
# print(list_1)
# print(len(list_1))
# if i == len_max:
#     print(len_max)
for i in range(len(list_1)):
    # print(i + 1, list_1[i])
    if i == len_max:
        print(f" {i + 1} {len_max}")
    # else:
    #     print(f"{i}")  # {len[i]}
    print(f"{i}{list_1[i]:>len_max}")  # {len[i]}
    pass