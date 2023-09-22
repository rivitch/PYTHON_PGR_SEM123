# -*- coding: utf-8 -*-
# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


import os


def split_file_path(file_path):
	file_name = os.path.basename(file_path)
	path = os.path.dirname(file_path)
	file_name, file_extension = os.path.splitext(file_name)
	return (path, file_name, file_extension)
# I:\GB\TASKS\PYTHON_PGR_SEM123\file.txt
file_path = 'GB/TASKS/PYTHON_PGR_SEM123/file.txt'
result = split_file_path(file_path)
print(result)
