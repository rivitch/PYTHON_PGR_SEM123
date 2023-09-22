# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста. 
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы. 
# ✔ Напишите преобразование в одну строку. 

text_1 = 'Hello, world!'
dict_1 = {smb: ord(smb) for smb in text_1}
dict_2 =({smb: ord(smb)} for smb in text_1)
print(dict_1)
print(type(dict_1))
print(dict_2)
print(*dict_2)
print(type(dict_2))


#-----------------------------
# text_1 = 'Hello, world!'
# for i in text_1:
#     dict_1 = ord(i)
# print(dict_1)