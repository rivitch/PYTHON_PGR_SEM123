#import random
from random import randint

res= False
def chess_module(chessboard):
    pass


list_row = []
list_col = []
#row = randint(1,8)
for i in range (1,9):       # случайный расклад горизонталь
    row = (randint(1,8))
    list_row.append(row)
print(list_row) 
for i in range (1,9):       # случайный расклад вертикаль
    col = (randint(1,8))
    list_col.append(col)
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
        #print(abs(list_row[i+1] - list_row[i])) 
        print(i,j)
        #print(list_row[i])
        if abs(i - j) != abs((i+1) - j):
            res= True  
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



