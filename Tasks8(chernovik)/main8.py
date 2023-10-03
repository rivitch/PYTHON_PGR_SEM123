# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle
from random import randint

# with open('text_data.txt', 'w', encoding='utf-8') as f:
#     print(list(f))
# def write_json(tree, directory):
# 	with open(directory, 'w') as f:
# 		json.dump(tree, f)
	
def crt():
    list_1 = ['json','csv', 'pickle']
    #directory = os.getcwd()
    #for i in tree:
    #print(len(tree[0][2]))
    for j in list_1:
            file_name = (f'new8.{j}')
            f = open(file_name, 'w', buffering=64)
            #f.write()
            f.close()
    print("файлы созданы")

directory = os.getcwd()  # Получаем текущий рабочий каталог
print(directory)
tree = os.walk(directory)
#print(tree)

for i in tree:
    for j in i:
    #print(type(i))
        print(j)
        print(len(j))
    #break
        #print(len([i][j]))
    #print(i)
#crt()
# write_json(tree, directory)

# def read_json(directory):
# 	with open(directory, 'r') as f:
# 		return json.load(f)





