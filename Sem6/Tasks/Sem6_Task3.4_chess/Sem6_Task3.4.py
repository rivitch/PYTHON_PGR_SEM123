from chess_mod.chess import check
#import chess_mod
#from chess_mod import chess

list_res = []
for a in range(4):
    list_res.append(check())
#print(list_res)
for i in range(4):
    print(f'{i+1} - {list_res[i]}')

# for i in range(4):
#     print(f'результат :\n{check()}\n')