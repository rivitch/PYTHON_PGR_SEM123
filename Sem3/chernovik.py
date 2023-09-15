# В большой текстовой строке подсчитать количество встречаемых 
# слов и вернуть 10 самых частых. Не учитывать знаки препинания 
# и регистр символов. За основу возьмите любую статью 
# из википедии или из документации к языку
import os, shutil
from pprint import pp

_inp1 = 'file.txt'
# this_dir = os.path.dirname(os.path.abspath(__file__))
# file = os.path.join(this_dir, _inp1)
data = open(_inp1, 'r')
for line in data:
    print(line)
data.close()


# #_inp1 = "Qwerte kkl 87bv qwerte jtk kkl btj fsts mny ljj, hre kkl."
# _inp2 = _inp1.lower()
# # _list2 = _inp.split()
# # print(_inp,"\n", _list2)
# symbols_to_remove = ",!?."
# for symbol in symbols_to_remove:
#     _inp2 = _inp2.replace(symbol, "")
# _list1 = _inp2.split() # досюда работает
# print(_list1)
# print(_list1.count("qwerte"))
# res = []
# for i in _list1:
#     if _list1.count(i) >1:
#         res.append(i)
#         res = list(set(res))




# for i in _list1:
#     res.append(_list1.count(i))
# for spam, eggs in enumerate(res, 1):
#         #if spam not in (x, y, z):
#         print(f"{spam}. {eggs : >2}")    
#res.append(_list1.count("qwerte"))
# print("1", res)
# z=0 
# 
# for i in _list1:
#     print(i)
#     for j in range(len(_list1)):
#         #print(j, res)
#         res = []
#         _list1.count(i)
#         res[j] = z
#         print(i, j)
#         #pass
    #pass    
# print(res)