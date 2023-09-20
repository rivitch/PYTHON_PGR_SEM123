a = [1,2,3]
b = [1,2,3]
c = []
bu = (c.append((i+j)) for i in a for j in b)
# for i in a:
#     for j in b:
#         c.append((i+j))  
print(bu)
for char in bu:
    print(char)
