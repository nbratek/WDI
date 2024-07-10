from random import randint

def pierwsze(x):
    while x > 0:
        a = x % 10
        if a == 2 or a == 3 or a == 5 or a == 7:
            return True
        x //= 10
    return False

def liczby(tab):
    for n in tab:
        if pierwsze(n) is False:
            return False
    return True

def f(T):
    for i in range(len(T)):
        if liczby(T[i]) is True:
            return True
    return False

T = [[randint(0, 100) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(f(T))