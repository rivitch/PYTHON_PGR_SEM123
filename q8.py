import json
a = 'Hello world!'
for key, value in enumerate(a):
    b = {key: value}
    print(type(b), b)
    z = json.dumps(b, indent=3, separators=('; ', '= '))
    #print(f'{key}: {value}')
print(type(z), z)
x = {key: value for key, value in enumerate(a)}
y = json.dumps(x, indent=3, separators=('; ', '= '))
print(type(y), y)
print(type(x), x)