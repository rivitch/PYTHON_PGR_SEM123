def func():
    N = int(input('Введите число простых чисел: '))
    n = [2]
    for i in range(3,100):
        count =0
        for j in n:
            if i%j == 0 :
                count += 1
        if count<1:
            n.append(i)
        if len(n)==N:
            break
        yield 
    # print('20 ',n)
    # print(len(n))
func()