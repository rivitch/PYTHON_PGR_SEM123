from random import randint
list_row = []
list_col = []
res= False
def chess_module():
    res= False

    #list_row = (randint(1,8) for i in range (1,9))
    for i in range (1,9):       # случайный расклад горизонталь
        row = (randint(1,8))
        list_row.append(randint(1,8))
    print(list_row) 
    #list_col = (randint(1,8) for i in range (1,9))  
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
            #print(i,j)
            #print(list_row[i])
            if abs(i - j) != abs((i+1) - (j+1)):
                res= True  
    if res == True:
        return res
print(chess_module())
# if res == True:

#     #x,y = (list_row, list_col)
#     pass

#         #ass  