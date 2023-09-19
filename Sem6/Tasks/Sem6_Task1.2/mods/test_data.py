""""""
from mods.test import bis_sextus


def f_test_data():
    list_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day,month,year,*_ = input("\nВведите дату в формате DD.MM.YYYY: ").split('.')
    print(f'проверка високосности : {bis_sextus(year)}')
    if bis_sextus(year):
        list_month[1] = 29
        print("год високосный!")
    if 0<int(month)<=12 and 0<int(day)<=int(list_month[int(month)-1]): 
        print('есть такая дата')
        return True 
    else:
        print('такой даты не существует')
        return False
    
# #----------------------------------------------------------
# def f_test_data():


#     list_month = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
#     day,month,year,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')
#     print(f'проверка високосности : {bis_sextus(year)}')
#     #list_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#     #list_month = ((1,31),(2,28),(3,31),(4,30),(5,31),(6,30),(7,31),(8,31),(9,30),(10,31),(11,30),(12,31))
#     if bis_sextus(year):
#         list_month[1][1] = 29
#         print("год високосный!")
#         #print(list_month)
#     # print(type(month))
#     # print(list_month[int(month)-1][1])
#     if 0<int(month)<=12 and 0<int(day)<=int(list_month[int(month)-1][1]): 
#         print('есть такая дата')
#         return True 
#     else:
#         print('такой даты не существует')
#         return False




#-------------------------------------------------------------
# 
#     
    # for value in list_month.items():
    #     if 0<int(month)<=12 and 0<int(day)<=int(value): 
    #         print('есть такая дата')
    #         return True 
    #     else:
    #         print('такой даты не существует')
    #         return False
        
#---------------
#          # print(key, value, month, day)
        # print(type(key), type(value), type(month), type(day))        
    #print(key, value, month, day)  

    #print(type(key), type(value), type(month), type(day))
    # for i in range(1,13):
    #     if 0<day<=list_month.values():
    #         print('есть такая дата')



    # for key in list_month.keys():
    #     if key == month
    #     print(key)
    # #     for value in list_month.value():







    # if not bis_sextus(year):
    #     #for i in range(list_month[i]):


    #     print('пошли дальше')
    # elif bis_sextus(year): 
    #     pass
    # else:
    #     print('такой даты не существует')    

    #for i in 
    #pass


#_LIST_MONTH = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]