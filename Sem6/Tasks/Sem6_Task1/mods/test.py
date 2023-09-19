
# _START_YEAR = 0
# _END_YEAR =10000

def  bis_sextus(year) -> bool:   # проверка на високосный год
    #day,month,year,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')
    x = int(year)
    print(f'{x} год н.э.')
    if x<0 or x>10000: 
    #if int(year)<_START_YEAR or int(year)>_END_YEAR:   #_START_YEAR>int(year)>_END_YEAR:
        print("ошибка!") 
        return
    elif x%4 == 0 and x%400 == 0:
        print("год високосный!")
        return True
    else:
        print("год не високосный!")
        return False
       

# #_LIST_MONTH = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30,[12,31]]]


# def  bis_sextus(year) #-> bool:   # проверка на високосный год

#     #return bool 