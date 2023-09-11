# Задание №1
# ✔ Напишите функцию, которая принимает строку текста. 
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого 
# длинного слова был один пробел между ним и номером строки.

def _1():
    _str1 = "Напишите функцию, которая принимает строку текста."
    list_1 = _str1.split()
    len_max =len(max(list_1, key=len))
    #x, y, z = " ", ".", ","
    for spam, eggs in enumerate(list_1, 1):
        #if spam not in (x, y, z):
        print(f"{spam}. {eggs : >{len_max}}") 
_1()   
    #pass

# _str1 = "Напишите функцию, которая принимает строку текста."
# def _1(data: str):
#     list_1 = data.split()
#     len_max =len(max(list_1, key=len))
#     list_1.sort()
#     for spam, eggs in enumerate(list_1, 1):
#         print(f"{spam}. {eggs :>{len_max}}")
# print(_1(_str1)) # None?  
   