from itertools import chain, combinations
items = {'спальник': 5.0, 'палатка': 10.0, 'топор': 2.5, 'едаэ': 7.0, 'влда': 5.0,'радио': 3.0}
capacity = int(input('Грузоподъёмность рюкзака'))
backpack = 0
pack =[]
for name, weight in items.items():
    if backpack + weight <= capacity:
        backpack += weight
        pack.append(name)
pack.append(backpack)
print(pack)