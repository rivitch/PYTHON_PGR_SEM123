# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типо
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

# from pprint import pp
# turple_1 = (1, 2, 3, False, True, False, None, "qwerty", {1,2,3}, [1,2], 4.5, 3.14) # {1,2,3},
# out = dict()
# print(turple_1)
# for i in turple_1:
#     # print(i)
#     if type(i) not in out:
#         # print(type(i))
#         out[type(i)] = []
#         # print(out)
#     out[type(i)].append(i)
#     print(out)
# pp(out)    

# # через setdefault
# from pprint import pp
# turple_1 = (1, 2, 3, False, True, False, None, "qwerty", {1,2,3}, [1,2], 4.5, 3.14) # {1,2,3},
# out = dict()
# for i in turple_1:
#     out.setdefault(type(i),[])
#     out[type(i)].append(i)
# pp(out)    

# через цикл
from pprint import pp
turple_1 = (1, 2, 3, False, True, False, None, "qwerty", {1,2,3}, [1,2], 4.5, 3.14) # {1,2,3},
out = dict()
for item in turple_1:
    if type(item) in out:
        out[type(item)].append(item)
    else:
        out[type(item)] = [item]
pp(out)        