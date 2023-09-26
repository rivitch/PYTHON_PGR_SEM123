
from random import randint
#import chess_diagonal
#from . import chess_diagonal
#from chess_mod. chess_diagonal import chess_diagonal

# list_left_up = []
# list_left_down = []
res= False


# def chess():
#     list_res = []
#     count_4 = 0
#     for a in range(4):
#         list_res.append(chess_module())
#     #list_res.append(chess_module())
#     print(f'list_res - {list_res}')


def chess_diagonal(list_1):
    print(f'list_1 - {list_1}')
    print(f'list_1[0][0] - {list_1[0][0]}')
    #list_1 = [(5, 5)]
    list_left_up = []
    list_left_down = []
    # for a in list_tuple:
    #     list_1 = [a]
    #     print(list_tuple)
    #     print(a)
    #     # list_left_up = []
    #     # list_left_down = [] 
    #     #for b in a:
    for i in range(1,list_1[0][0]):
        if 0<(list_1[0][0]-i and list_1[0][1]-i)<9:
            list_left_up.append((list_1[0][0]-i, list_1[0][1]-i))
    for i in range(1, 9-list_1[0][1]):
        if 0<(list_1[0][0]+i and list_1[0][1]+i) < 9:
            list_left_up.append((list_1[0][0]+i, list_1[0][1]+i)) # работает
    print(sorted(list_left_up))   
#___
    for i in range(1,list_1[0][0]):
        if 0<(list_1[0][0]-i and list_1[0][1]+i)<9:
            list_left_down.append((list_1[0][0]-i, list_1[0][1]+i))
    for i in range(1, 9-list_1[0][0]):
        if 0<(list_1[0][0]+i and list_1[0][1]-i) < 9:
            list_left_down.append((list_1[0][0]+i, list_1[0][1]-i))
    print(sorted(list_left_down))
    return   list_left_up,list_left_down


list_4 = []
list_4_count = 0
count= 0
while res==False and list_4_count != 4:
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
        # print(f'list_row - {list_row}')
        # print(f'list_col - {list_col}')
        # print(f'list_tuple - {list_tuple}')

    if (len(set(list_row))) == (len(list_row)) and (len(set(list_col))) == (len(list_col)):
        res= True
        print(f'ферзи по вертикали и горизонтали не бьют друг друга  - {res}')
    else:
        res= False
        print(f'новый вариант - {res}')
        continue
    #list_left_up, list_left_down = chess_diagonal(list_tuple)
    # print(f'диагональ слевавверх - {list_left_up}')

    # print(f'диагональ слевавниз - {list_left_down}')
    for i in list_tuple:
        #print(f'list_tuple[i] - {list_tuple[i]}')
        print(f'list_row - {list_row}')
        print(f'list_col - {list_col}')
        print(f'list_tuple - {list_tuple}')
    
        print(f'list_tuple[0][0] - {list_tuple[0][0]}')
        i= list([i])
        print(f'i - {i}')
        print(f'i[0][0] - {i[0][0]}')
        list_left_up, list_left_down = chess_diagonal(i)
        print(f'диагональ слевавверх - {list_left_up}')
        print(f'диагональ слевавниз - {list_left_down}')
        #list_left_up.append(i)
        for j in (list_left_up or list_left_down):
            if i==j:
                res= False
                print(f'новый вариант - {res}')
                continue
        if res == True:
            list_4_count += 1
            list_4.append(list_tuple)
            print(f'ферзи по диагонали не бьют друг друга  - {res}')
    # if res == True:
    #     list_4_count += 1
    #     list_4.append(list_tuple)
    #     print(f'ферзи по диагонали не бьют друг друга  - {res}') 
    # if list_4_count == 4:
    #     break      
                # res= True
                # list_4_count += 1
                # list_4.append(list_tuple)
                # print(f'ферзи по диагонали не бьют друг друга  - {res}')
        # if i in (list_left_up or list_left_down):
        #     res= False
        #     print(f'новый вариант - {res}')
        #     continue
        # else:
        #     res= True
        #     list_4_count += 1
        #     list_4.append(list_tuple)
        #     print(f'ферзи по диагонали не бьют друг друга  - {res}')
        # if list_4_count == 4:
        #     break

#list_left_up, list_left_down = chess_diagonal()
#print(f'возврат функции \n{chess_diagonal()}')
# print(f'диагональ слевавверх - {list_left_up}')

# print(f'диагональ слевавниз - {list_left_down}')
print(list_tuple)
#for i in      


print(f'{list_col}\n{list_row}')  
if res==False:
    print(f'Ферзи бьются: {res}')
else:
    print(f'Ферзи не бьются: {res}') 
print(list_4)  

