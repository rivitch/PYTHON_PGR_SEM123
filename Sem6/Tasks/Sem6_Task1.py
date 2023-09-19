a,b,c,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')

if 0<year<10000:
    print("ошибка!")
elif y%4 == 0 and ((y%100 != 0) or (y%400)) == 0:
    print("год високосный!")
else:
    print("год не високосный!")