



day,month,year,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')

def  bis_sextus(year):   # gh
    print(int(year))
    if 0<int(year)>10000:
        print("ошибка!") 
    elif int(year)%4 == 0 and int(year)%400 == 0:
        print("год високосный!")
    else:
        print("год не високосный!")

bis_sextus(year)