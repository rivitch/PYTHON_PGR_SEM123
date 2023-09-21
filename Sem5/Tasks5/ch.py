# -*- coding: utf-8 -*-
def func():
    N = int(input('Введите число простых чисел: '))
    list = [2]    # первое простое 
    #list_q = [2]
    n =5
    for i in range(n):
        print(i, n)
        for j in list:
            if i%j != 0:
                list.append(n)
    n+=1
    print(f'{list}\n{n}')         
        # print(f'{list}\n{n}')        
        # yield; n+=1                 
            # else:
            #     n+=1
            # pass

# # n = 3
# # list_q.append(n)

# # print(f'{list}\n{list_q}')

# #+++++++++++++++++++++=
# # # -*- coding: utf-8 -*-
# # print("\n3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.\nИспользуйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. \nСделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.\n")

# # n = ""
# # j = 0
# # while n.isdigit()==False or 0<=int(n)>100000:
# #     n = input("Введите неотрицательное число и не больше 100000 : ")   
# # r = int(n)+1
# # for i in range(2,r):
# #     if int(n)%i == 0 :
# #         j=j+1
# #     #print(int(n),int(n)%i,i,j,r)
# # if j>1:
# #     print("\nЧисло составное")
# # elif int(n)==0 or int(n)==1:
# #     print("\nЧисла 0 и 1 не являются ни простыми, ни составными")    
# # else:
# #     print("\nЧисло простое")
# # print("\nEND\n")   


# #=====================
# # a = [1,2,3]
# # b = [1,2,3]
# # c = []
# # bu = (c.append((i+j)) for i in a for j in b)
# # # for i in a:
# # #     for j in b:
# # #         c.append((i+j))  
# # print(next(bu))
# # for char in bu:
# #     print(char)

# #N = int(input('Введите число простых чисел: '))
# # list = [2]    # первое простое 
# # list_q = [2]
# # _CONST = 10
# #n =0

# #z=(n+=1 while n!= N)
# #print(z)
# # while n!= N:
# #     n+=1
# #     print(n)
#     #pass
