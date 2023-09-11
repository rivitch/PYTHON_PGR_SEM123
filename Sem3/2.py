

from pprint import pp
my_list = "Cтрока, которую вводит пользователь текста."
# my_list1 = my_list
# len_x = len(my_list)
# for i in my_list1:   #range(len_x):
#     if i != (" " or "," or "."):
#         my_list1= list.pop([i])
#         #my_list1.add(i)
print(my_list)        
# print(x := sorted(my_list))  # Выводится сортированный словарь
out = dict()
res = dict()
for i in my_list:
    if i != ("."):# or i != (",") or i != (" "):
        if i != (" "):
            if i != (","):
                if i in out:
                    out[i].append(i)
                    #print(f"символ {i} добавился ")
                else:
                    out[i] = [i]
                    #print(f"добавился новый ключ {i}")
                z = len(out[i])
                res[i]= [z]
                #print(res)
#pp(f"{x}")
pp(res)
