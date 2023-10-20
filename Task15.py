"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. 
Соберите информацию о содержимом в виде объектов namedtuple. 
Каждый объект хранит: 
○ имя файла без расширения или название каталога, 
○ расширение, если это файл, 
○ флаг каталога, 
○ название родительского каталога. 
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import os
import logging
# import shutil
from collections import namedtuple

logging.basicConfig(filename='log.txt', filemode='w', level=logging.INFO)  #Sem15/
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])
#print(FileInfo)

def print_directory(path):
    contents = os.listdir(path) #+ '\Sem15'
    #print(type(contents))
    #print(contents)
    for item in contents:
        item_path = os.path.join(path, item)
        #print(item_path)
        if os.path.isfile(item_path):
            name, extension = os.path.splitext(item)
            is_directory = False
        elif os.path.isdir(item_path):
            name, extension = item, ''
            is_directory = True
        else:
            continue
        parent_directory = os.path.basename(path)
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        logging.info(f'Name: {file_info.name}, Extension: {file_info.extension}, '
        f'Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}')
        if is_directory:
            print_directory(item_path)
directory_path = input("Введите путь до директории: ")

print_directory(directory_path)

# python I:\GB\TASKS\PYTHON_PGR_SEM123\Sem15\Task15.py
# I:\GB\PROGRAMMS\Python38\Lib\logging