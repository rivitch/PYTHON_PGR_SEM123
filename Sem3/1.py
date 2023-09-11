my_list = "Cтроку вводит пользователь текста"
# sort_list = sorted(my_list)
# print(sort_list)
print(x := sorted(my_list))
# print(x := _inp.sorted())
# print(len(_inp))
out = dict()
for i in x:
    if i in out:
        
        out[i].append(i)
        # y = len(out[i])
        # y += 1
        # out[i] = [y]
        print(f"символ {i} добавился ")
    else:
        out[i] = [i]
        print(f"добавился новый ключ {i}")
    y = len(out[i])
    out[i] = [y]    
    print(f"{out}")
    pass
# #print(num := _inp.count("т"))
#print(f"{out}")
print(out[" "], len(out[" "]))