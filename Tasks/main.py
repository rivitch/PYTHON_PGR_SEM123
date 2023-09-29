# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
# from random import randint
from file_mod.f_renm import rnm, crt

end_name = input("желаемое конечное имя файлов : ")
num = input("количество цифр в порядковом номере : ")
a = input("расширение исходного файла : ")
b = input("расширение конечного файла : ")
x,y,*_ = input("диапазон сохраняемого оригинального имени в формате 'X Y': ").split()


directory = os.getcwd()  # Получаем текущий рабочий каталог
print(directory)
#crt() # работает
rnm(end_name, num, a, b, x, y) 

