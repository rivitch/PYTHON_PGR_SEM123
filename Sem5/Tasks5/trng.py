txt = '1234567'
res = [i for i in txt]
print(res, type(res))
res = {i for i in txt}
print(res, type(res))
res = (i for i in txt)
print(res, type(res))
print(*res, type(res))

