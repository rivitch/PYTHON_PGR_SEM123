"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. 
"""


from mods.test_data import f_test_data

print(f'результат :{f_test_data()}\n')



#-------------------------------------------------

# #from mods.test import bis_sextus
# from mods.test_data import f_test_data


# print(f'результат :{f_test_data()}')
# #day,month,year,*_ = input("введите дату в формате DD.MM.YYYY: ").split('.')


# def t():
#     pass        


# #print(bis_sextus())
# #print(bis_sextus(year))