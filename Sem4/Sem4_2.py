# Задание №2
# ✔ Напишите функцию, которая принимает строку текста. 
# ✔ Сформируйте список с уникальными кодами Unicode каждого 
# символа введённой строки отсортированный по убыванию.

_str1 = "Напишите функцию, которая принимает строку текста."
def F4_2(data: str):
    my_list = sorted(data)
    set_list = sorted(list(set(my_list)),reverse=True)
    res = []
    for i in set_list: 
        res.append([ord(i),i])
    # for spam, eggs in enumerate(set_list, 0):
    #     print(f"{ord(eggs)} - {eggs}")
    return res
print(F4_2(_str1))
#print(type(F4_2(_str1)))


# ---
# семинарское
#print([ord(i) for i in sorted(list(set(_str1)))])
print([ord(i) for i in sorted(list(set(_str1)), reverse= True)]) # по убыванию
# ---------
# my_list = sorted(_str1)
# #set_list = {}
# # set_list = set(my_list)
# # set_list=sorted(list(set(my_list)))
# #print(type(my_list),my_list,"\n",type(set_list),set_list)
# set_list = sorted(list(set(my_list)),reverse=True)
# # print(type(set_list))
# # print(type(my_list),my_list,"\n",type(set_list),set_list,"\n")
# for spam, eggs in enumerate(set_list, 0):
#     print(f"{ord(eggs)} - {eggs}")



# _str1 = "Напишите функцию, которая принимает строку текста."
# my_list = sorted(_str1)
# #set_list = {}
# # set_list = set(my_list)
# # set_list=sorted(list(set(my_list)))
# #print(type(my_list),my_list,"\n",type(set_list),set_list)
# set_list = sorted(list(set(my_list)),reverse=True)
# # print(type(set_list))
# # print(type(my_list),my_list,"\n",type(set_list),set_list,"\n")
# for spam, eggs in enumerate(set_list, 0):
#     print(f"{ord(eggs)} - {eggs}")
#---
# #print(set_list[0])
# # set_list = list(set_list)
# # print(type(my_list),my_list,"\n",type(set_list),set_list)
# # _str1 = "Напишите функцию"  #, которая принимает строку текста."
# # def F4_2(data: str):
# #     my_list = sorted(data,reverse=True)
# #     set_list = {my_list}
# #     for i in my_list:

# #         pass
# #     #res = 
# #     return my_list
# # print(F4_2(_str1))
