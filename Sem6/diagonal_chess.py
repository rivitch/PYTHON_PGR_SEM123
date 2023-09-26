


list_1 = [(5, 5)]
list_left_up = []
list_left_down = []
# x, y = list(map(int,input(f'координаты - ').split()))
#print(list_1[0][1]) # есть доступ
# print(type(list_1[0])) # кортеж
for i in range(1,list_1[0][0]):
    if 0<(list_1[0][1]-i and list_1[0][0]-i)<9:
        list_left_up.append((list_1[0][0]-i, list_1[0][1]-i))
    #list_left_up.append((list_1[0][0]+i, list_1[0][1]+i))
for i in range(1, 9-list_1[0][1]):
    if 0<(list_1[0][1]+i and list_1[0][0]+i) < 9:
    #print(list_1[0][1],i)
        list_left_up.append((list_1[0][0]+i, list_1[0][1]+i)) # работает
    #list_left_up.append((list_1[0][0]-i, list_1[0][1]-i))
print(sorted(list_left_up))   
#___
for i in range(1,list_1[0][0]):
    if 0<(list_1[0][0]-i and list_1[0][1]+i)<9:
        #print((list_1[0][0]-i, list_1[0][1]+i))
        list_left_down.append((list_1[0][0]-i, list_1[0][1]+i))
        #print('дошли')
    #list_left_up.append((list_1[0][0]+i, list_1[0][1]+i))
for i in range(1, 9-list_1[0][0]):
    #print(list_1[0][1],i)
    if 0<(list_1[0][0]+i and list_1[0][1]-i) < 9:
        #print(list_1[0][0]+i, list_1[0][1]-i)
        list_left_down.append((list_1[0][0]+i, list_1[0][1]-i))
#     #list_left_up.append((list_1[0][0]-i, list_1[0][1]-i))
#print(list_left_down)  
print(sorted(list_left_down))  


