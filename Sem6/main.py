# import base_math
from mathematical import base_math as bm
from mathematical.advanced_math import exp

# x = base_math.mul # Плохой приём   - x не является понятным для других разработчиков именем
                  # multiplication = base_math.mul 
multiplication = bm.mul
x = bm.div(12, 5)     
# y = base_math._START_MULT # Очень плохой приём  - Не используйте защищённые и приватные объекты за пределами модуля, в
                          # котором они созданы. Особенное если это не ваш модуль. Исключение —
                          # прописанное в модуле указание на использование
y = bm._START_MULT
# z = base_math.sub(73, 42)
# z = bm.sub(73, 42)
z = exp(2, 3)
x = bm.div(12, 5)

print(x(2, 3))
print(y)
print(z)