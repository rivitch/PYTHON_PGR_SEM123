# # 13_1 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число. 📌Обрабатывайте не числовые данные как исключения.

# def number_input():
#     while True:
#         try:
#             user_input = input("Введите число: ")
#             number = float(user_input)
#             if number.is_integer():
#                 return int(number)
#             else:
#                 return number
#         except ValueError:
#             print("Ошибка! Введите целое или вещественное число.")

# number = number_input()
# print("Вы ввели число:", number)

# # --------------------------------------------------------------
# # 13_2 Создайте функцию аналог get для словаря. Помимо самого словаря функция принимает ключ и значение по умолчанию. При обращении к несуществующему ключу функция должна возвращать дефолтное значение. Реализуйте работу через обработку исключений.

# def get_from_dict(dictionary, key, default='Значение не найдено'):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return default

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# value = get_from_dict(my_dict, 'b')
# print(value)
# value = get_from_dict(my_dict, 'd')
# print(value)

# ----------------------------
# # 13_3 Создайте класс с базовым исключением и дочерние классыисключения: ○ ошибка уровня, ○ ошибка доступа.

class BaseException(Exception):
    def handle_exception(self):
        print("Обработка базового исключения")

# class LvlErr(BaseException):
#     def ex(self):
#         print("Обработка ошибки уровня")
class LvlErr(BaseException):
    def __init__(self, message, level):
        super().__init__(message)
        self.level = level

    def handle_exception(self):
        super().handle_exception() # вызываем метод handle_exception() родительского класса
        print("Дополнительная обработка ошибки уровня")
class AccessErr(BaseException):
    def ex(self):
        print("Обработка ошибки доступа")

# try:
#     raise AccessErr("Ошибка уровня!")
# except BaseException as e:
#     print(type(e).__name__ + ": " + str(e))

try:
    raise LvlErr("Ошибка уровня!")
except BaseException as e:
    e.ex()

#+++++++++++
# class LvlErr(BaseException):
#     def __init__(self, message, level):
#         super().__init__(message)
#         self.level = level

# def handle_exception(self):
#     super().handle_exception() # вызываем метод handle_exception() родительского класса
#     print("Дополнительная обработка ошибки уровня")

error = LvlErr('Ошибка уровня!') # , 3
print(error.message)
print(error.level)
error.handle_exception()