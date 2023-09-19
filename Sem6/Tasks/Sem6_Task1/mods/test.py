
_START_YEAR = 0
_END_YEAR =10000
#_LIST_MONTH = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30,[12,31]]]


def  bis_sextus(year) -> bool:   # проверка на високосный год
    print(int(year))
    if _START_YEAR<int(year)>_END_YEAR:
        print("ошибка!") 
    elif int(year)%4 == 0 and int(year)%400 == 0:
        print("год високосный!")
    else:
        print("год не високосный!")
    #return bool 