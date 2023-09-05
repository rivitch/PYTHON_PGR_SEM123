print("\nНапишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.\nПрограмма должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions\n")

from math import gcd 

first_fraction = input("Введите первую дробь : ").split("/")
sec_fraction = input("Введите вторую дробь : ").split("/")

a=int(first_fraction[0])
b=int(first_fraction[1])
x=int(sec_fraction[0])
y=int(sec_fraction[1])
z= gcd((a*x),(b*y))
q= gcd((a*y)+(x*b),(b*y))
#print(f"Произведение дробей равно : {(int(first_fraction[0])*int(sec_fraction[0]))//(int(first_fraction[1])*int(sec_fraction[1]))}")
#print(z,q)
if b*y//z==1:
    print(f"\nПроизведение дробей равно : {a*x//z}")
else:
    print(f"\nb Произведение дробей равно : {((a*x)//z)}/{((b*y)//z)}")
if b*y//q==1:
    print(f"Cумма дробей равна : {((a*y)+(x*b))//q}")
else:
    print(f"Cумма дробей равна : {((a*y)+(x*b))//q}/{(b*y)//q}")
# Проверяем результат
import fractions
print("\nПроверка с помощью модуля fractions : ")
print(f"Произведение дробей равно : {fractions.Fraction(a,b)*fractions.Fraction(x,y)}")
print(f"Cумма дробей равна : {fractions.Fraction(a,b)+fractions.Fraction(x,y)}")
print("\nEND")
"""
S.split(символ)

"""