# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами
# ✔ Сформируйте список с порядковыми номерами 
# нечётных элементов исходного списка. 
# ✔ Нумерация начинается с единицы.

my_list = [3, 4, 1, 2, 8, 10, 10, 9, 2, 4, 14, 3]
out = []
count = 0
print(my_list)
my_list_1 = list(enumerate(my_list))
my_list_2 = list(enumerate(my_list, start=1))
# print(list(enumerate(my_list)))
# print(list(enumerate(my_list, start=1)))
for item in my_list:
    # print(item, my_list_2[item])
    if item%2 != 0:
        # print(f"число {item} нечетное : ",item%2)
        count += 1
        out.append([count, item])
        # print(f"{my_list[count]}\n")
        # out.append([(my_list.index(item)), item])
print(out)     

# for item in my_list:
#     print(item, my_list[item])
#     if item%2 != 0:
#         print("нечетное : ",item%2)
#         # count += 1
#         # out.append([count, item])
#         # print(f"{my_list[count]}\n")
#         out.append([(my_list.index(item)), item])
# print(out)     
# # out.append((my_list.index(item)) + 1, item)

# for item in my_list:
# #for i in range(len(my_list)):
#     for i in range(len(my_list)):
#     #for item in my_list:
#         print(i, item)
#         if item%2 != 0:
#             print("нечетное : ",item%2)
#         # count += 1
#         # out.append([count, item])
#         # print(f"{my_list[count]}\n")
#             out.append([i, item])
#             print(f"{out}") 
# print(out)     
# # out.append((my_list.index(item)) + 1, item)