
from math import sqrt
from random import randint
import csv
from typing import Callable
import json


# def m_cwadro(a,b,c):        # квадратное уравнение  #a, b, c  # работает
#     d = (b**2)-(4*a*c)
#     if d>0 :
#         x1=float((-b+ sqrt(d))/(2*a))
#         x2=float((-b- sqrt(d))/(2*a))
#         print(x1, x2)
#     elif d ==0:
#         x1=float(-b/(2*a))
#         print(x1)
#     else:
#         print('нет решений')
#     return 

def m_file_create():    # работает
    for i in range(1, 11):
        a = randint(1,11)
        b = randint(1,11)
        c = randint(1,11)
        #m_cwadro(a,b,c)
        with open('new9.csv', 'a', newline='', encoding='utf-8') as f_write:
            csv_write = csv.writer(f_write, dialect='excel-tab', delimiter=',',quoting=csv.QUOTE_MINIMAL)
            line = (a,b,c)
            csv_write.writerow(line)    
    #return csv_write

def m_file_read(): # работает
    #print(csv_write[2][2])
    with open('new9.csv', 'r', newline='', encoding='utf-8') as f_read:
        csv_file = csv.reader(f_read)
        for line in csv_file:
            #print(type(line))
            #m_cwadro(a,b,c)
            #print(line, line[0])  #type(line), 
            a = int(line[0])
            b = int(line[1])
            c = int(line[2])
            d = (b**2)-(4*a*c)
            if d>0 :
                x1=float((-b+ sqrt(d))/(2*a))
                x2=float((-b- sqrt(d))/(2*a))
                print(x1, x2)
            elif d ==0:
                x1=float(-b/(2*a))
                print(x1)
            else:
                x3 = 'нет решений'
                print(x3)
            f_write = open('new9a.csv', 'a', newline='', encoding='utf-8')
            #with open('new9a.csv', 'a', newline='', encoding='utf-8') as f_write:
            csv_write = csv.writer(f_write, dialect='excel-tab', delimiter=',',quoting=csv.QUOTE_MINIMAL)
            line_1 = (a,b,c,x1,x2,x3)
            csv_write.writerow(line_1)        
    # with open('new9.csv', 'a', newline='', encoding='utf-8') as f_write:
    #     csv_write = csv.writer(f_write, dialect='excel-tab', delimiter=',',quoting=csv.QUOTE_MINIMAL)
    #     line = (a,b,c)
    #     csv_write.writerow(line)                
            #print(m_cwadro(int(line[0]),int(line[1]),int(line[2])))
            #print(csv_file)


def m_json():

    pass


#m_file_create()
m_file_create()
m_file_read()
            #csv_write.writerows(f_write)

            #print(line)  #работает
            # all_data = []
            # for i in enumerate(all_data):
            #     if i == 0:
            #         csv_write.writerow(line)   #)print(
            #     else:
            #         line[2] += 1
            #         for j in range(2, 4 + 1):
            #             line[j] = int(line[j])
            #             all_data.append('{line}\n')
            #     print(all_data)
            # print(all_data)
            #csv_write.writerows(all_data)
        # with open('new_data.txt', 'a', encoding='utf-8') as f:
        #     for line in text:
        #         print(line, file=f)

#a, b, c, *_ = input(f'введите 3 числа').split()
#print(a,b,c, type(a))
#cwadro(int(a),int(b),int(c))
