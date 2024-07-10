from random import randint
def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i - 1 <= int(n ** 0.5) + 1:
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
        i += 6
    return True

def komplementarne(T):
    n = len(T)
    T2 = [[0 for _ in range(n)] for _ in range(n)]
    suma = 0 
    for i in range(n):
        for j in range(n - 1): 
            suma = T[i][j] + T[i][j + 1]
            if prime(suma):
                T2[i][j] = T[i][j]
                T2[i][j + 1] = T[i][j + 1]
    return T2


T = [[randint(0, 10) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(komplementarne(T))