# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

# # случайный список
# number = []
# from random import randint
# number_rnd = []
# for i in range(10):
#     number_rnd.append((randint(1,10)))
# for i in range(10):    
#     if i not in number_rnd:
#         number.append(i)
# print(f"{number}\n{number_rnd}")

# Ввод списка вручную
number = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
number_inp = []
for i in number:    
    if i not in number_inp:
        number_inp.append(i)
print(f"{number}\n{number_inp}")

