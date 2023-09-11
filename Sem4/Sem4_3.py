# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число. 
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

from pprint import pp
_str1 = "35 55"

def F4_3(data: str):
    list_1 = data.split()
    for i in range(len(list_1)):
        list_1[i] = int(list_1[i])
    list_1.sort()
    dict_1 = {chr(i): i for i in range(list_1[0],(list_1[1]+1))}
    return dict_1
pp(F4_3(_str1))
#--- 




# # #------
# # # семинарское (не работает)
# def f4_3(_str: str):# -> dict:
#     res = sorted([int(i) for i in _str.split()])
#     # return {chr[i]: i for i in range(res[0], res[1] + 1)}
#     return {chr[i]: i for i in range(min(res), max(res) + 1)}
#     #pass
# print(f4_3("35 55"))