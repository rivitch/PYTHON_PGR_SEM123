
import os
from random import randint

# end_name = input("желаемое конечное имя файлов : ")
# num = input("количество цифр в порядковом номере : ")
# a = input("расширение исходного файла : ")
# b = input("расширение конечного файла : ")
# x,y,*_ = input("диапазон сохраняемого оригинального имени в формате 'X Y': ").split()



def crt():
    os.mkdir('new_os_dir')
    for i in range(10000,10002):
        file_name = (f'new_os_dir/{i}.txt')
        f = open(file_name, 'wb', buffering=64) # encoding='utf-8',
        f.write(b'X' * randint(1, 20))
        # f = open(file_name, 'r', encoding='utf-8')
        # print(list(f))
        f.close()
    print("каталог создан")


def rnm(end_name = None, num = None, a = None, b = None, x = None, y = None):
    crt()
    print('получил')
    pass
