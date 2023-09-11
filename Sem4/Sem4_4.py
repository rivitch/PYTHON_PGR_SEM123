# Задание №4
# ✔ Функция получает на вход список чисел. 
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

from random import randint
my_list = []
for i in range(10):
    my_list.append(randint(0, 10))
    #print(my_list[i])
print(my_list)
# def F4_4(x):

#     pass
# print(F4_4(my_list))

# семинарное (сортировка пузырьком)
def my_sort(some_lst:list):
    for i in range(len(some_lst)):
        for j in range(len(some_lst) -i -1):
            if some_lst[j] > some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j+ 1], some_lst[j]
    return some_lst
my_sort(my_list)
print(my_list)   


