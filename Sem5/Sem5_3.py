# Задание №3
# ✔ Продолжаем развивать задачу 2. 
# ✔ Возьмите словарь, который вы получили. 
# Сохраните его итераторатор. 
# ✔ Далее выведите первые 5 пар ключ-значение, 
# обращаясь к итератору, а не к словарю.

text_1 = 'Hello, world!'
dict_1 = {smb: ord(smb) for smb in text_1}
#dict_2 =({smb: ord(smb)} for smb in text_1)
print(dict_1)
#iter_dict = iter(dict_1)
print(iter(dict_1))
print(iter(dict_1.items()))
print(iter(dict_1.keys()))
print(iter(dict_1.values()))
for i in range(5):
    print(next(iter(dict_1)))