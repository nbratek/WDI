from random import randint 

def suma(T):
    n = len(T)
    x, y = 0, 0
    max_suma = 0
    for i in range(n):
        for j in range(n):
            suma = 0 
            if i - 1 >= 0:
                suma += T[i - 1][j]
                if j - 1 >= 0:
                    suma += T[i - 1][j - 1]
                if j + 1 < n:
                    suma += T[i - 1][j + 1]
            if i + 1 < n:
                suma += T[i + 1][j]
                if j - 1 >= 0:
                    suma += T[i + 1][j - 1]
                if j + 1 < n:
                    suma += T[i + 1][j + 1]
            if j - 1 >= 0:
                suma += T[i][j - 1]
            if j + 1 < n:
                suma += T[i][j + 1]
            if max_suma < suma:
                max_suma = suma
                x = j 
                y = i
    return x, y

T = [[randint(0, 10) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(suma(T))
