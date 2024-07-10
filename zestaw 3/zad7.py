from random import randint

def dlugosc(x): 
    l = 0
    while x > 0:
        l += 1
        x //= 10
    return l 

def nieparzyste(x):
    licznik = 0
    while x > 0:
        a = x % 10 
        if a % 2 == 1:
            licznik += 1
            x //= 10
        else:
            x //= 10
    return licznik

def f(N):
    T = [randint(1, 1000) for _ in range(N)]
    for i in range(N): 
        print(T[i])
    for i in range(N):
        if dlugosc(T[i]) == nieparzyste(T[i]):
            return True
    return False



n = int(input())
print(f(n))