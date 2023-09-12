# Семинар 4, ДЗ 1.
# Напишите функцию для транспонирования матрицы

from copy import deepcopy
_matrix = [[1,2,3],["a","b","c"],[3.14, "qwer", 5]]
def Fmap(data):
    for i in range(len(data)):
        print(data[i])
Fmap(_matrix)
res = deepcopy(_matrix)
#from pprint import pp # не сработало
# pp(f"{_matrix[0]")
def Fmatrix(data:list):
    #res = deepcopy(data)
    for i in range(len(data)):
        #print("i = ", i)
        for j in range(len(data[i])):
            #print("j = ", j)
            #print(data[j][i])
            #res.append(data[j][i])
            res[j][i] = data[i][j]
            #print(res,"\n")    
    return res
#print("\n", Fmatrix(_matrix))
#pp(Fmatrix(_matrix))
#print(Fmap(Fmatrix(_matrix)))
print()
Fmap(Fmatrix(_matrix))