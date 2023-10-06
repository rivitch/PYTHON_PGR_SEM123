# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle
from random import randint
#import mod8.func

# with open('text_data.txt', 'w', encoding='utf-8') as f:
#     print(list(f))
# def write_json(tree):
# 	with open(tree, 'w') as f:
# 		json.dump(tree, f)

def m_data(tree):
    for i in tree:
        with open('data.txt', 'a', encoding='utf-8') as f:  
            #json.dump('\nОкончание файла', f, ensure_ascii=False) #  ensure_ascii=False
            #f = open('Sem7/2file_sem7.txt', 'a', encoding='utf-8')
            f.write(str(i))

            #f.write()
            f.close()
        print(i)
        print(f'i = {type(i)}\n{len(i)}') 
    pass

def main_create():
    list_1 = ['json','csv', 'pickle']
    #directory = os.getcwd()
    #for i in tree:
    #print(len(tree[0][2]))
    for j in list_1:
            file_name = (f'new8.{j}')
            #f = open(file_name, 'w', buffering=64)
            
            with open(file_name, 'a', encoding='utf-8') as f:  
                json.dump('\nОкончание файла', f, ensure_ascii=False) #  ensure_ascii=False
            #f = open('Sem7/2file_sem7.txt', 'a', encoding='utf-8')
            #f.write('\nОкончание файла')

            #f.write()
            f.close()
    print("файлы созданы")

directory = os.getcwd()  # Получаем текущий рабочий каталог
print(directory)
tree = os.walk(directory)
#print(tree)

# for i in tree:
#     print(i)
#     print(f'i = {type(i)}\n{len(i)}')
m_data(tree)
#for i in tree:
    #if i ({'I:\\GB\\TASKS\\PYTHON_PGR_SEM123\\Tasks7'} or {'I:\\GB\\TASKS\\PYTHON_PGR_SEM123\\Tasks7'}):
        #for j in i:
    #print(type(i))
            #print(j)
            #print(len(j))
    #break
        #print(len([i][j]))
    #print(i)
#main_create()
#write_json(tree)

# def read_json(directory):
# 	with open(directory, 'r') as f:
# 		return json.load(f)





