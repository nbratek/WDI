from random import randint

def f(T):
    n = len(T)
    max_suma = 0
    for i in range(n):
        k = 0 
        w = 0
        for j in range(n):
            w += T[i][j]
            k += T[j][i]
            if j > 9:
                w -= T[i][j -10]
                k -= T[j - 10][i]
            if w > max_suma:
                max_suma = w
            if k > max_suma:
                max_suma = k 
    return max_suma


T = [[randint(-20, 20) for _ in range(14)]for _ in range(14)]
for i in range(14):
    print(T[i])

print(f(T))