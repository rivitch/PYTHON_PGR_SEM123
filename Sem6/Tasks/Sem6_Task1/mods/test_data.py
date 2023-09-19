
from mods.test import bis_sextus

def f_test_data():
    day,month,year,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')
    print(f'проверка високосности : {bis_sextus(year)}')
    if bis_sextus(year):
        print('пошли дальше')
    else:
        print('такой даты не существует')    

    #for i in 
    #pass


#_LIST_MONTH = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30,[12,31]]]