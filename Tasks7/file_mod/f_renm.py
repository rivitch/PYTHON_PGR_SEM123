"""
def crt()  - Функция создания файлов
def rnm()  - Функция переименования файлов
"""
import os
from pathlib import Path
from random import randint
import shutil

file_list = []

def crt():
    #os.mkdir('new_os_dir')
    list_1 = ['txt','doc', 'jpeg']
    for i in range(10000,10002):
        for j in list_1:
            file_name = (f'{i}.{j}')
            file_list.append(file_name)
            f = open(file_name, 'wb', buffering=64) # encoding='utf-8',
            f.write(b'X' * randint(1, 20))
            f.close()
    print("файлы созданы")
    print(file_list)


def rnm(end_name, num, a, b, x, y = None):

    directory = os.getcwd()  
    print(directory)
    for filename in os.listdir(directory):

        if filename.endswith(a):
            original_name = filename[:int(y)]
            new_name = f"{end_name}_{original_name}_"
            for i in range(1, int(y) + 1):
                #print(type(i), type(num), num)
                if i <= int(num):
                    new_name += '0'
            new_name += str(i)
            new_name += f".{b}"
            
            os.rename(filename, new_name)
            print(filename, new_name)
       

