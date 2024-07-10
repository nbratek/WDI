from random import randint

def f(T):
    x, y = 0,0 
    a, b = 0, 0
    max_suma = 0 
    n = len(T)
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n):
                for m in range(n):
                    if k != i:
                        suma = 0 
                        for l in range(n):
                            suma += T[i][l]
                            suma += T[l][j]
                            suma += T[k][l]
                            suma += T[l][m]
                        suma -= T[i][j]
                        suma -= T[k][m]
                        suma -= T[i][m]
                        suma -= T[k][j]
                if max_suma < suma:
                    max_suma = suma
                    x, y = i, j
                    a, b = k, m
    return x, y, a, b




T = [[randint(0, 20) for _ in range(7)]for _ in range(7)]
for i in range(7):
    print(T[i])

print(f(T))