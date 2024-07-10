from math import sqrt

def sito(N):
    T = [True for _ in range(N + 1)]
    T[0] = T[1] = False
    for i in range(2, int(sqrt(N))+ 1):
        if T[i] is True:
            for j in range(i * i, N + 1, i):
                T[j] = False
    for i in range(2, N + 1):
        if T[i] is True:
            print(i)

n = int(input())
print(sito(n))
