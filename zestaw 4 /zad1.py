def spirala(T, N):
    m = N
    if m % 2 == 1:
        m += 1
    m //= 2
    idx = 0
    p = 0
    k = N - 1 
    for i in range(m):
        for j in range(i, N - i):
            T[i][j] = idx
            idx += 1
        for j in range(i + 1, N - i):
            T[j][N - 1 - i] = idx
            idx += 1
        for j in range (1 + i, N - i):
            T[N - i - 1][N - 1 - j] = idx
            idx += 1
        for j in range(i + 1, N - 1 - i):
            T[N - j - 1][i] = idx
            idx += 1
    return T

N = 4
T = [[0 for _ in range(N)]for i in range(N)]
print(spirala(T, N))