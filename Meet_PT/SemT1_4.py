print("Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. ")
print("Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, ")
print("если известно, что Петя и Сережа сделали одинаковое количество журавликов, ")
print("а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?")
print("*Пример:*")

print("6 -> 1  4  1")
print("24 -> 4  16  4")
print("    60 -> 10  40  10")

S = int(input("Введите общее количество журавликов: "))
Pit = S//6
Kate = S-Pit*2
Srj = Pit
print(S,"->",Pit,Kate,Srj)