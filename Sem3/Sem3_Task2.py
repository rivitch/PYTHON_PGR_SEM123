# В большой текстовой строке подсчитать количество встречаемых 
# слов и вернуть 10 самых частых. Не учитывать знаки препинания 
# и регистр символов. За основу возьмите любую статью 
# из википедии или из документации к языку

from pprint import pp
_list1 = ["Qwerte kkl 87bv qwerte jtk kkl btj fsts mny ljj, hre kkl."]
res = []
print(len(_list1[0])) 
print(_list1)
for i in _list1:
    for j in range(len(_list1)):
        # res[j] = _list1.count(i)
        # print(i, j)
        pass
    pass    
print(res)