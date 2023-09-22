a = 2
b = [2]
print(max(b))
#===============
#for i in range(min(b), max(b)+1):
    #print(i,min(b), max(b))
for j in range(3,20):
    #print(f'a = {a+1} i = {i}')
    for i in range(min(b), max(b)+1):
        print(j, i,min(b), max(b)+1)
    #for j in range(2,100):
        if j%int(i) != 0:
            print('qwer', j,i)
            b.append(j)
            print(b)
            #print(f'b = {b}')
            
            #print(f'a = {a}')   
        if len(b)==17:
            break
    a+=1

# for i in range(min(b), max(b)+1 ):
#     print(i,min(b), max(b))
# #for j in range(2,100):
#     print(f'a = {a+1} i = {i}')
#     #for i in range(min(b), 10 ):
#     for j in range(2,100):
#         if j%int(i) != 0:
#             b.append(j)
#             #print(f'b = {b}')
            
#             #print(f'a = {a}')   
#         if len(b)==17:
#             break
#     a+=1
#print(b)

# for i in range(min(b), 10 ):#max(b)
#     a += 1
#     print(f'a = {a} i = {i}')
#     if a%int(i) != 0:
#         b.append(a)
#         print(f'b = {b}')
        
#         print(f'a = {a}')    
#         if len(b)==17:
#             break
#print(b)        










#================
# a = 2
# b = [2]
# for i in range(min(b), 10 ):#max(b)
#     a += 1
#     print(f'a = {a} i = {i}')
#     if a%int(i) != 0:
#         b.append(a)
#         print(f'b = {b}')
        
#         print(f'a = {a}')    
#         if len(b)==17:
#             break
#print(b)        