
from random import randint
 

def chess_diagonal(list_1):
    list_left_up = []
    list_left_down = []
    for i in range(1,list_1[0][0]):
        if 0 < (list_1[0][0]-i and list_1[0][1]-i) < 9:
            list_left_up.append((list_1[0][0]-i, list_1[0][1]-i))
    for i in range(1, 9-list_1[0][1]):
        if 0 < (list_1[0][0]+i and list_1[0][1]+i) < 9:
            list_left_up.append((list_1[0][0]+i, list_1[0][1]+i)) # работает   
#___
    for i in range(1,list_1[0][0]):
        if 0 < (list_1[0][0]-i and list_1[0][1]+i) < 9:
            list_left_down.append((list_1[0][0]-i, list_1[0][1]+i))
    for i in range(1, 9-list_1[0][0]):
        if 0 < (list_1[0][0]+i and list_1[0][1]-i) < 9:
            list_left_down.append((list_1[0][0]+i, list_1[0][1]-i))
    return   list_left_up,list_left_down

def check():
    res=False
    count= 0    
    while res==False:  # and list_4_count != 4
        x = 8
        list_row = []
        list_col = []
        list_tuple = []
        count +=1 
        print(f'Работаю. Вариантов проверено - {count}')
        for i in range (1,x+1):
            list_row.append(randint(1,x))    # случайный расклад горизонталь
            list_col.append(randint(1,x))    # случайный расклад вертикаль 
            list_tuple.append((list_col[i-1], list_row[i-1]))   # кортеж для диагонали

        if (len(set(list_row))) == (len(list_row)) and (len(set(list_col))) == (len(list_col)):
            res= True
            print(f'ферзи по вертикали и горизонтали не бьют друг друга  - {res}')
        else:
            res= False
            continue
        for i in list_tuple:
            i= list([i])
            list_left_up, list_left_down = chess_diagonal(i)
            for j in (list_left_up or list_left_down):
                if i==j:
                    res= False
                    continue
    if res == True:
        print(f'ферзи по диагонали не бьют друг друга  - {res}')
        return list_tuple
    

# list_res = []
# for a in range(4):
#     list_res.append(check())
# #print(list_res)
# for i in range(4):
#     print(f'{i+1} - {list_res[i]}')