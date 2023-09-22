N = int(input('Введите число простых чисел: '))
list_1 = [2]    # первое простое 
#list_q = [2]
#a = 2


def func(a, b, c): 
    #a += 1
    print(min(b), max(b))
    # c = 0
    # b = []
    #b_1 = 
    print(type(a), type(b), type(c))
    for i in range(min(b), max(b)):
            print(i)
            if a%int(i) != 0:

                b.append(a)
                print(b)
                a += 1
                print(a)    
    # while c != len(b):
    #     #print(c , len(b))
    #     for i in range(min(b), max(b)):
    #         print(i)
    #         if a%int(i) != 0:

    #             b.append(str[a])
    #             print(b)
    #             a += 1
    #             print(a)
    #         # # else:
    #         # #     a += 1



func(3, list_1, N)
# print(f'end{list_1}')

# def func():    
    # N = int(input('Введите число простых чисел: '))
    # list = [2]    # первое простое 
    # #list_q = [2]
    # a =5
#     for j in list:
        
#         for i in range(2,a):
#             print(i, a)
#             if j%i != 0:
#                 list.append(a)
#                 a += 1
#         #yield n
# # for i in range(2,n):
# #     print(i, n)
# #     for j in list:
# #         if i%j != 0:
# #             list.append(n)
# #             n+=1
# #print(f'{list}\n{n}')         