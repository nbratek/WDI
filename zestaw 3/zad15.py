from math import sqrt

def pierwsze(x): 
    if x < 2: 
        return False
    for i in range(2, int(sqrt(x)) + 1): 
        if x % i == 0: 
            return False
    return True

def fib(T):
    flaga = False
    a, b = 1, 2 
    i = 0
    while i < len(T): 
        if i == a: 
            if pierwsze(T[i]):
                return False
            a, b = b, a + b
        else: 
            if pierwsze(T[i]):
                flaga = True
        i += 1
    return flaga

T = [12, 32, 24, 6, 7, 90, 33, 45, 80, 11]
print(fib(T))

