# _list1 = [2,3,4,[4,5]] # список (НТП)
# _list2 = _list1
# # _list1.append(a) # ссылка на самого себя  - [2, 3, 4, [4, 5], [...]]
# _list1.append(4)
# # ----
# _list2 = _list1.copy() # копия первого уровня
# _list1.append(4)
# _list1[3][0] = "вкп"
# # ---
# from copy import deepcopy
# b = deepcopy(_list1) # полная копия 
# _list1.append(4)
# _list1[3][0] = "выкл"
# # ---
# _tuple1 = (2,3,4,[4,5]) # кортеж (ИТП)(не изменяется только верхний уровень)
# _tuple2 = _tuple1
# # print (type(_tuple2), _tuple2)
# _tuple1[3][0] = "раз"
# _tuple1 += (1.5, "qwerty")
# ----
from pprint import pp
_matr1 = [[1,2,3],[1,2,3],[1,2,3]] # матрица
# ошибки в кортеже
_matr2 = [1,2,3]
_matr2[2] = 16
pp(_matr2)
_matr3 = [_matr2,_matr2,_matr2]
_matr3[2][0] = "A"


# print (_list1)
# print (_list2)
# print (_tuple1)
# print (_tuple2)
pp(_matr2)
pp(_matr3)
#----


#print(f"{F_my(a}={x,b}={y}))")
#print(F_my(a=x,b=y))
#   for value, key in kwargs.items():