#import random
from random import randint

res= False
def chess_module(chessboard):
    pass
list_row = []
list_col = []
list_4 = []
count= 0
while res==False:
    count +=1 
    print(f'Работаю. Вариантов проверено - {count}')
    #row = randint(1,8)
    list_row = (randint(1,8) for i in range (1,9))
    # for i in range (1,9):       # случайный расклад горизонталь
    #     list_row.append(randint(1,8))
    #     #yield list_row
    print(list_row)   # вытаскивать через next
    list_col = (randint(1,8) for i in range (1,9))   
    # for i in range (1,9):       # случайный расклад вертикаль
    #     list_col.append(randint(1,8))
    print(list_col) 
    if (len(set(list_row))) == (len(list_row)): # проврпка горизонтали (одинаковых нет)
        print('ферзи по горизонтали не бьют друг друга')
        res= True
    if (len(set(list_col))) == (len(list_col)): # проверка вертикали (одинаковых нет)
        print('ферзи по вертикали не бьют друг друга')
        res= True
    for i in list_row:   # проверка диагоналей
        for j in list_col:
            #print(abs(list_row[i+1] - list_row[i])) 
            #print(i,j)
            #print(list_row[i])
            if abs(i - j) != abs((i+1) - (j+1)):
                print('успешно')
                res= True
                list_4.append(list_row,list_col)
                if len(list_4)==4:
                    print(list_4) 
    if res == False:
        list_row.clear
        list_col.clear

                  
        #ass  
    # print(list_row)
    # print(set(list_row)) 
    # print(len(set(list_row))) 
    #if i in row:

print(f'{list_row}\n{list_col}')  
if res==False:
    print(f'Ферзи бьются: {res}')
else:
    print(f'Ферзи не бьются: {res}') 
    # list_4.append(i,j)
    # if len(list_4)==4:
print(list_4)  
print(f'{list_row},{list_col}')
#-------------------
# for i in range (1,9):       # случайный расклад
#     row, col = ((randint(1,8)),(randint(1,8)))
#     list_1.append((row,col))
# print(list_1[5])
#     # for i in range (1,9):
#     #     print(set(list_1[i]))

# print(list_1)      
# # check_row = set(list_1) 
# # print(check_row)   
    
# # print(f'{list_1}\n{row}\n{col}')    



