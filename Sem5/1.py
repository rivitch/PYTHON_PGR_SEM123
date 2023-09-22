'''✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''

# def prime_generator(N):
#     count = 0
#     number = 2
#
#     while count < N:
#         is_prime = True
#
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             yield number
#             count += 1
#
#         number += 1
#
#
# for prime in prime_generator(10):
#     print(prime)

'''==============================================================================================================='''
'''✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''

# import os
#
#
# def split_file_path(file_path):
# 	
# 	file_name = os.path.basename(file_path)
#
# 	
# 	path = os.path.dirname(file_path)
#
# 	
# 	file_name, file_extension = os.path.splitext(file_name)
#
# 	return (path, file_name, file_extension)
#
# file_path = '/path/to/file.txt'
# result = split_file_path(file_path)
# print(result)


'''==========================================================================================================='''
'''✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
'''
# names = ["John", "Alice", "Bob"]
# bets = [100, 200, 150]
# rewards = ["10.25%", "5.5%", "8.75%"]
#
# dictionary = {name: bet * float(reward.strip("%")) / 100 for name, bet, reward in zip(names, bets, rewards)}
# print(dictionary)

'''==============================================================================================================='''
''' Создайте функцию генератор чисел Фибоначчи
'''
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()
for i in range(5):
    print(next(fib))