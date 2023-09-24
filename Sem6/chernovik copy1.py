
from random import randint

res= False
def chess_module(chessboard):
    pass

list_4 = []
count= 0
while res==False:
    x = 8
    y = 8
    list_row = []
    list_col = []
    count +=1 
    print(f'Работаю. Вариантов проверено - {count}')

    for i in range (1,x+1):       # случайный расклад горизонталь
        list_row.append(randint(1,x))
    print(list_row)   # вытаскивать через next

    for i in range (1,y+1):       # случайный расклад вертикаль
        list_col.append(randint(1,y))
    print(list_col) 
#+++++++++++++++++  
    if (len(set(list_row))) == (len(list_row)) and (len(set(list_col))) == (len(list_col)):
        res= True
        print(f'ферзи по вертикали и горизонтали не бьют друг друга  - {res}')
    else:
        res= False
        print(f'новый вариант - {res}')
        continue 
    for i in range (x):
        if list_row[i] == list_col[i]:
            res= False
            print(f'новый вариант - {res}')
            continue  
        else:
            res= True
            print(f'ферзи по диагонали не бьют друг друга  - {res}')
#++++++++++++++++++++++++++
print(f'{list_row}\n{list_col}')  
if res==False:
    print(f'Ферзи бьются: {res}')
else:
    print(f'Ферзи не бьются: {res}') 
print(list_4)  
