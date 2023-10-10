# -*- coding: utf-8 -*-
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.

print("\n2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.\nДано a,b,c, - стороны предпологаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой \nдвух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами\nне существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.\n")

class Triangle:
	
	def __init__(self, a,b,c):
		self.a = a
		self.b = b
		self.c = c
		
	def check(self, *args, **kwargs):
		#a,b,c = map(int,input("Введите стороны треугольника a,b и c, разделенные знаком пробела : ").split(" ",2))
		if a==0 or b==0 or c==0 or a+b<=c or a+c<=b or b+c<=a:
			res = "Треугольника не существует"
		elif a==b==c:
			res = "Треугольник равносторонний"
		elif a==b or b==c or a==c:
			res = "Треугольник равнобедренный" 
		else:
			res = "Треугольник разносторонний"
		return res
	pass

a,b,c = map(int,input("Введите стороны треугольника a,b и c, разделенные знаком пробела : ").split(" ",2))
x = Triangle(a,b,c)

print(x.check())