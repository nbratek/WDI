from math import inf 
from random import randint 

def iloraz(T):
    n = len(T)
    max_kol = 0
    min_w = inf 
    x = 0
    y = 0 
    for i in range(n):
        suma_w = 0
        for j in range(n):
            suma_w += T[i][j]
        if min_w > suma_w:
            min_w = suma_w
            y = i
    for i in range(n):
        suma_k = 0
        for j in range(n):
            suma_k += T[j][i]
        if max_kol < suma_k:
            max_kol = suma_k
            x = i
    return x, y

T = [[randint(1, 10) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])
print(iloraz(T))