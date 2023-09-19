print("Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек ")
print("отломить k долек, если разрешается сделать один разлом по прямой ")
print("между дольками (то есть разломить шоколадку на два прямоугольника). ")
print("*Пример:*")

print("3 2 4 -> yes")
print("3 2 1 -> no ")

print("")
flag = "no"
size1 = ""
size2 = ""
dol =""
while size1.isdigit()==False or size2.isdigit()==False or dol.isdigit()==False:
    size1,size2,dol=input("Введите размеры шоколадки и количество долек, разделенные знаком пробела :").split()
if ((int(dol)/int(size1)).is_integer() or (int(dol)/int(size2)).is_integer()) and int(size1)*int(size2)!=int(dol):
    flag = "yes"
print(size1,size2,dol,"->",flag)