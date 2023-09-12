# Семинар 4, ДЗ 1.
# Напишите функцию для транспонирования матрицы

from copy import deepcopy
_matrix = [[1,2,3],["a","b","c"],[3.14, "qwer", 5]]

def Fmap(data):
    for i in range(len(data)):
        print(data[i])

Fmap(_matrix)
res = deepcopy(_matrix)
# from pprint import pp # не сработало
# pp(_matrix)
# pp(f"{_matrix[0]")

def Fmatrix(data:list):
    for i in range(len(data)):
        for j in range(len(data[i])):
            res[j][i] = data[i][j]
    return res

print()
Fmap(Fmatrix(_matrix))