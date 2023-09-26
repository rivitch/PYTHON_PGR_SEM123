# def chess_diagonal(list_1):
#     print(f'list_1 - {list_1}')
#     print(f'list_1[0][0] - {list_1[0][0]}')
#     #list_1 = [(5, 5)]
#     list_left_up = []
#     list_left_down = []
#     # for a in list_tuple:
#     #     list_1 = [a]
#     #     print(list_tuple)
#     #     print(a)
#     #     # list_left_up = []
#     #     # list_left_down = [] 
#     #     #for b in a:
#     for i in range(1,list_1[0][0]):
#         if 0<(list_1[0][0]-i and list_1[0][1]-i)<9:
#             list_left_up.append((list_1[0][0]-i, list_1[0][1]-i))
#     for i in range(1, 9-list_1[0][1]):
#         if 0<(list_1[0][0]+i and list_1[0][1]+i) < 9:
#             list_left_up.append((list_1[0][0]+i, list_1[0][1]+i)) # работает
#     print(sorted(list_left_up))   
# #___
#     for i in range(1,list_1[0][0]):
#         if 0<(list_1[0][0]-i and list_1[0][1]+i)<9:
#             list_left_down.append((list_1[0][0]-i, list_1[0][1]+i))
#     for i in range(1, 9-list_1[0][0]):
#         if 0<(list_1[0][0]+i and list_1[0][1]-i) < 9:
#             list_left_down.append((list_1[0][0]+i, list_1[0][1]-i))
#     print(sorted(list_left_down))
#     return   list_left_up,list_left_down