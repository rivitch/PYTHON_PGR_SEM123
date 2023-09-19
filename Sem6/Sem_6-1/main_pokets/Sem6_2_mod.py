from random import randint


def fchance(low, up, n) -> bool:
    num = randint(low, up)
    z = None
    for i in range(1,n+1):
        print("Попытка №",i)
        n = int(input("Угадайте число : "))
        if num==n:
            print("Поздравляю!")
            z = True
            break
        elif num>n:
            print("больше")
        elif num<n:
            print("меньше")
    if num!=n:
        print("Казнить, объяснительную и, чтоб к завтрему был как штык!")
        z = False
    return z

if __name__ == '__main__':
    print(fchance(0, 1000, 10))  