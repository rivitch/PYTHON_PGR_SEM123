# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

_inp = "Cтроку вводит пользователь текста"
# print(_inp)
list_1 = _inp.split()
# len_max = max(list_1, key=len)
len_max =len(max(list_1, key=len))+1
# print(len_max, "/",list_1)
count = 0

for i in list_1:
    count += 1
    if i == len_max:
        print(f"{count}. {i : >{len_max}}") # {i + 1}," ",
    else:
        print(f"{count}.{i : >{len_max}}")  # {len[i]}

# через enumerate()
list_1.sort()
for spam, eggs in enumerate(list_1, 1):
    print(f"{spam}.{eggs : >{len_max}}")
    # pass

# # max = int(len_max)
# print(type(len_max), len_max)
# #x = int(len(len_max))
# # print(type(x))
# # print(x)
# list_1.sort()
# print(list_1)
# print(len(list_1))
# for i in list_1:
#     # print(i + 1, list_1[i])
#     print(i, type(i))
#     print(len_max, type(len_max))
#     if i == len_max:
#         print(f"{i + 1} {len_max}")
# # if i == len_max:
# #     print(len_max)
# # for i in range(len(list_1)):
# #     # print(i + 1, list_1[i])
# #     print(i, type(i))
# #     print(len_max, type(len_max))
# #     if i == len_max:
# #         print(f"{i + 1}," ",{x}")
#     # else:
#     #     print(f"{i}")  # {len[i]}
# #print(f"{i}{list_1[i] = :> key}")   
#     #print(f"{i}{list_1[i] = :> key}")  # {len[i]}
#     #pass