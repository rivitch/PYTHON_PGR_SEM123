# В большой текстовой строке подсчитать количество встречаемых 
# слов и вернуть 10 самых частых. Не учитывать знаки препинания 
# и регистр символов. За основу возьмите любую статью 
# из википедии или из документации к языку

from pprint import pp
#_inp1 = 'file.txt'
_inp1 = "Qwerte kkl 87bv qwerte jtk kkl btj fsts mny ljj, hre kkl."
_inp2 = _inp1.lower()
symbols_to_remove = ",!?."
for symbol in symbols_to_remove:
    _inp2 = _inp2.replace(symbol, "")
_list1 = _inp2.split() # досюда работает
print(_list1)
print(_list1.count("qwerte"))
res = []
for i in _list1:
    if _list1.count(i) >1:
        res.append(i)
        res = list(set(res))
print("1", res)
