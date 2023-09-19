
# _START_YEAR = 0
# _END_YEAR =10000

def  bis_sextus(year) -> bool:   # проверка на високосный год
    #day,month,year,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')
    x = int(year)
    #print(f'{x} год н.э.')
    if x<0 or x>10000: 
    #if int(year)<_START_YEAR or int(year)>_END_YEAR:   #_START_YEAR>int(year)>_END_YEAR:
        print("ошибка!") 
        return
    elif x%4 == 0 and x%400 == 0:
        #print("год високосный!")
        return True
    else:
        #print("год не високосный!")
        return False
       
