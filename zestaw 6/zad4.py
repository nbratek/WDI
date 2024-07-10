def skoczek(T, w = 0, k = 0, n = 1):
    T[w][k] = n 
    if n == (len(T)) ** 2:
        return True
    moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (2, -1), (1, -2), (-1, 2)]
    for i in moves:
        next_w = w + i[0]
        next_k = k + i[1]
        if contains(T, next_w, next_k) and T[next_w][next_k] == 0:
            if skoczek(T, next_w, next_k, n + 1):
                return True
    T[w][k] = 0
    return False

def contains(T, w, k):
    if 0 <= w < len(T) and 0 <= k < len(T):
        return True
    return False

T2 = [[0 for _ in range(6)] for _ in range(6)]
skoczek(T2)
for row in T2:
    print(row)