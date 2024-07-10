from random import randint
def kwadrat(T, k):
    n = len(T)
    for a in range(2, n, 2):
        for i in range(n):
            for j in range(n):
                if i + a < n and j + a < n: 
                    if T[j][i] * T[j][i + a] * T[j + a][i] * T[j + a][i + a] == k: 
                        return True, j + a / 2, i + a / 2
    return False

k = int(input())
T = [[randint(0, 10) for _ in range(7)]for _ in range(7)]
for i in range(7):
    print(T[i])

print(kwadrat(T, k))