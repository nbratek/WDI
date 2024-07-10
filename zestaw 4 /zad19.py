from random import randint
def f(T, k):
    n = len(T)
    licznik = 0
    for i in range(n): 
        for j in range(n):
            if i + 2 < n and j + 1 < n:
                if T[i][j] * T[i + 2][j + 1] == k:
                    licznik += 1
            if i + 2 < n and j - 1 >= 0:
                if T[i][j] * T[i + 2][j - 1] == k:
                    licznik += 1
            if i - 1 >= 0 and j + 2 < n:
                if T[i][j] * T[i - 1][j + 2] == k:
                    licznik += 1
            if i + 1 < n and j + 2 < n:
                if T[i][j] * T[i + 1][j + 2] == k:
                    licznik += 1
    return licznik
k = int(input())
T = [[randint(0, 10) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(f(T, k))
