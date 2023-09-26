# Дан список повторяющихся элементов. Вернуть список 
# с дублирующимися элементами. В результирующем списке 
# не должно быть дубликатов.

_list1 = input("Введите список элементов, разделенных пробелом: ").split()
out = []
#_list1 = [2, 4, 6, 2, 8, 10, 10, 12, 2, 4, 14, 2]

#out = (x = out.append(i) for i in _list1 if _list1.count(i) > 1)# AttributeError: 'generator' object has no attribute 'append'
for i in _list1:
    if _list1.count(i) > 1:
        out.append(i)
print(list(set(out)))